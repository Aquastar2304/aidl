"""
22AIE304 / Card I2 (Team 1) - Readiness note item 7.

Annex D0 Week-1 measurement table, row I2:
    "Official-fold 1-D CNN (17,073 training records)"
    (stage to project from a subset: none - "the five audit fits repeat it")

This is the no-attention 1-D CNN that Card I2 requires as its reference model and
that Core experiment 1 and the five audit fits reuse. It is not an extra experiment.

D0 limits honoured here:
  * default seed 22
  * at most 30 epochs OR 30 minutes elapsed wall-clock, whichever comes first;
    the clock runs from the first training batch to the end of the last validation
    pass and checkpoint save
  * early stopping after 5 validation checks without improvement
  * best-validation checkpoint retained
  * at most 250,000 trainable parameters
  * CPU only

Test labels and test metrics play NO part. The inference pass below runs over
test-SHAPED data and is timed only; no label is read and no metric is computed.

Usage: python -I 04_timed_reference_fit.py <out_dir> <cache_dir> [threads] [workers]
"""
import json
import os
import sys
import time

import numpy as np
import pandas as pd
import psutil
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset

OUT = os.path.abspath(sys.argv[1])
CACHE = os.path.abspath(sys.argv[2])
THREADS = int(sys.argv[3]) if len(sys.argv) > 3 else 6
WORKERS = int(sys.argv[4]) if len(sys.argv) > 4 else 0

SEED = 22
MAX_EPOCHS = 30
MAX_SECONDS = 30 * 60
PATIENCE = 5
BATCH = 128
SUPER = ["NORM", "MI", "STTC", "CD", "HYP"]

torch.manual_seed(SEED)
np.random.seed(SEED)
torch.set_num_threads(THREADS)

proc = psutil.Process()

# ------------------------------------------------------------------ data
ids = pd.read_csv(os.path.join(OUT, "I2_official_split_ids.csv"), index_col="ecg_id")
sig = np.load(os.path.join(CACHE, "signals_lr_f32.npy"), mmap_mode="r")
assert len(ids) == sig.shape[0], (len(ids), sig.shape)

part = ids["partition"].values
tr, va, te = part == "train", part == "val", part == "test"
Y = ids[SUPER].values.astype(np.float32)

t_prep = time.time()
Xtr = np.ascontiguousarray(sig[tr])
Xva = np.ascontiguousarray(sig[va])
Xte = np.ascontiguousarray(sig[te])

# training-only per-lead standardisation (D0: fitted preprocessing is refit from
# the training partition; never from validation or test)
mu = Xtr.mean(axis=(0, 2), keepdims=True)
sd = Xtr.std(axis=(0, 2), keepdims=True)
sd[sd == 0] = 1.0
for A in (Xtr, Xva, Xte):
    A -= mu
    A /= sd
scaler = {"mean_per_lead": mu.ravel().tolist(), "std_per_lead": sd.ravel().tolist()}
prep_seconds = time.time() - t_prep

ds_tr = TensorDataset(torch.from_numpy(Xtr), torch.from_numpy(Y[tr]))
ds_va = TensorDataset(torch.from_numpy(Xva), torch.from_numpy(Y[va]))
dl_tr = DataLoader(ds_tr, batch_size=BATCH, shuffle=True, num_workers=WORKERS,
                   generator=torch.Generator().manual_seed(SEED))
dl_va = DataLoader(ds_va, batch_size=256, shuffle=False, num_workers=WORKERS)


# ------------------------------------------------------------------ model
class ECG1DCNN(nn.Module):
    """No-attention 1-D CNN over 12 leads. The lead-wise channel-attention variant
    required by Card I2 adds its attention block to this exact backbone, so this
    fit doubles as that ablation."""

    def __init__(self, n_leads=12, n_out=5):
        super().__init__()

        def block(ci, co, k, pool):
            return nn.Sequential(
                nn.Conv1d(ci, co, k, padding=k // 2, bias=False),
                nn.BatchNorm1d(co), nn.ReLU(inplace=True), nn.MaxPool1d(pool))

        self.features = nn.Sequential(
            block(n_leads, 32, 7, 2),   # 1000 -> 500
            block(32, 64, 5, 2),        #  500 -> 250
            block(64, 128, 5, 2),       #  250 -> 125
            block(128, 128, 3, 2),      #  125 ->  62
            block(128, 128, 3, 2),      #   62 ->  31
        )
        self.head = nn.Sequential(nn.AdaptiveAvgPool1d(1), nn.Flatten(),
                                  nn.Dropout(0.3), nn.Linear(128, n_out))

    def forward(self, x):
        return self.head(self.features(x))


model = ECG1DCNN()
n_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
n_total = sum(p.numel() for p in model.parameters())
assert n_params <= 250_000, n_params

opt = torch.optim.Adam(model.parameters(), lr=1e-3)
lossf = nn.BCEWithLogitsLoss()

print("trainable params %d  (total %d; D0 cap 250000)" % (n_params, n_total))
print("train %d  val %d  test-shaped %d" % (tr.sum(), va.sum(), te.sum()))
print("threads=%d dataloader_workers=%d batch=%d seed=%d" % (THREADS, WORKERS, BATCH, SEED))
print("preprocessing (outside the fit clock): %.1fs" % prep_seconds)
print("")

# ------------------------------------------------------------------ the timed fit
hist, updates = [], 0
best = {"val_loss": float("inf"), "epoch": -1}
stopped_by = None
since_best = 0

c0 = proc.cpu_times()
t0 = time.time()                       # clock starts at the first training batch
for epoch in range(1, MAX_EPOCHS + 1):
    model.train()
    tl, nb = 0.0, 0
    ep0 = time.time()
    for xb, yb in dl_tr:
        opt.zero_grad(set_to_none=True)
        loss = lossf(model(xb), yb)
        loss.backward()
        opt.step()
        tl += loss.item()
        nb += 1
        updates += 1
        if time.time() - t0 > MAX_SECONDS:
            stopped_by = "30-minute elapsed wall-clock limit (mid-epoch)"
            break
    model.eval()
    vl, vb = 0.0, 0
    with torch.no_grad():
        for xb, yb in dl_va:
            vl += lossf(model(xb), yb).item()
            vb += 1
    tr_loss, va_loss = tl / max(nb, 1), vl / max(vb, 1)
    hist.append({"epoch": epoch, "train_loss": round(tr_loss, 5), "val_loss": round(va_loss, 5),
                 "updates_cum": updates, "epoch_seconds": round(time.time() - ep0, 1),
                 "elapsed_seconds": round(time.time() - t0, 1),
                 "rss_mb": round(proc.memory_info().rss / 1e6, 1)})
    print("epoch %2d  train %.5f  val %.5f  %.0fs  cum %.0fs  rss %.0fMB"
          % (epoch, tr_loss, va_loss, hist[-1]["epoch_seconds"],
             hist[-1]["elapsed_seconds"], hist[-1]["rss_mb"]), flush=True)

    if va_loss < best["val_loss"] - 1e-5:
        best = {"val_loss": va_loss, "epoch": epoch}
        torch.save({"model": model.state_dict(), "scaler": scaler, "epoch": epoch,
                    "val_loss": va_loss, "seed": SEED},
                   os.path.join(OUT, "I2_official_1dcnn_best.pt"))
        since_best = 0
    else:
        since_best += 1

    if stopped_by:
        break
    if since_best >= PATIENCE:
        stopped_by = "early stopping (%d validation checks without improvement)" % PATIENCE
        break
    if time.time() - t0 > MAX_SECONDS:
        stopped_by = "30-minute elapsed wall-clock limit (at epoch boundary)"
        break
if stopped_by is None:
    stopped_by = "epoch limit (%d epochs)" % MAX_EPOCHS

fit_elapsed = time.time() - t0         # includes the last validation pass + checkpoint save
c1 = proc.cpu_times()
fit_cpu = (c1.user - c0.user) + (c1.system - c0.system)
peak_rss = max(h["rss_mb"] for h in hist)

# ------------------------------------------------------------------ timed, UNSCORED inference
# Test-SHAPED data only. No label is loaded, no metric is computed, nothing here
# feeds any later choice.
model.load_state_dict(torch.load(os.path.join(OUT, "I2_official_1dcnn_best.pt"))["model"])
model.eval()
Xte_t = torch.from_numpy(Xte)
i0, ic0 = time.time(), proc.cpu_times()
n_out_rows = 0
all_finite = True
with torch.no_grad():
    for s in range(0, len(Xte_t), 256):
        out = model(Xte_t[s:s + 256])
        n_out_rows += out.shape[0]
        all_finite = all_finite and bool(torch.isfinite(out).all())
inf_elapsed = time.time() - i0
ic1 = proc.cpu_times()
inf_cpu = (ic1.user - ic0.user) + (ic1.system - ic0.system)

report = {
    "card": "I2", "team": 1,
    "configuration": ("Official-fold no-attention 1-D CNN over 12 leads, PTB-XL records100, "
                      "folds 1-8 train / fold 9 validation"),
    "seed": SEED,
    "trainable_parameters": n_params, "total_parameters": n_total, "d0_parameter_cap": 250000,
    "threads": THREADS, "dataloader_workers": WORKERS, "batch_size": BATCH,
    "train_records": int(tr.sum()), "val_records": int(va.sum()),
    "test_shaped_records": int(te.sum()),
    "preprocessing_seconds_outside_clock": round(prep_seconds, 1),
    "fit_elapsed_seconds": round(fit_elapsed, 1),
    "fit_cpu_seconds": round(fit_cpu, 1),
    "epochs_completed": len(hist), "optimisation_updates": updates,
    "updates_per_epoch": len(dl_tr),
    "stopped_by": stopped_by,
    "peak_rss_mb": peak_rss,
    "best_epoch": best["epoch"], "best_val_loss": round(best["val_loss"], 5),
    "first_epoch_train_loss": hist[0]["train_loss"], "last_epoch_train_loss": hist[-1]["train_loss"],
    "first_epoch_val_loss": hist[0]["val_loss"], "last_epoch_val_loss": hist[-1]["val_loss"],
    "validation_completed": True,
    "timed_unscored_inference_seconds": round(inf_elapsed, 2),
    "timed_unscored_inference_cpu_seconds": round(inf_cpu, 2),
    "inference_rows": n_out_rows, "inference_outputs_all_finite": all_finite,
    "test_metrics_computed": False,
    "history": hist,
}
with open(os.path.join(OUT, "I2_timed_reference_fit.json"), "w", encoding="utf-8") as fh:
    json.dump(report, fh, indent=2)

print("")
print("stopped by          : %s" % stopped_by)
print("epochs completed    : %d   updates: %d" % (len(hist), updates))
print("fit elapsed         : %.1fs   fit CPU: %.1fs (ratio %.2fx)"
      % (fit_elapsed, fit_cpu, fit_cpu / max(fit_elapsed, 1e-9)))
print("peak RSS            : %.0f MB" % peak_rss)
print("train loss          : %.5f -> %.5f" % (hist[0]["train_loss"], hist[-1]["train_loss"]))
print("val   loss          : %.5f -> %.5f (best %.5f @ epoch %d)"
      % (hist[0]["val_loss"], hist[-1]["val_loss"], best["val_loss"], best["epoch"]))
print("unscored inference  : %.2fs elapsed, %.2fs CPU, %d rows, all finite=%s, NO metric computed"
      % (inf_elapsed, inf_cpu, n_out_rows, all_finite))
