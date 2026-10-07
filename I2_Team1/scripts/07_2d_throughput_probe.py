"""
22AIE304 / Card I2 (Team 1) - throughput probe for the 24-hour programme projection.

Readiness-note item 7 ends: "Then project the total required programme against the
24-hour elapsed budget, including classical baselines and repeated inference."

Card I2 requires a 2-D CNN on per-lead scalograms or spectrograms stacked as
channels. Its cost is not bounded by the measured 1-D fit, so it is measured here
the way Annex D0 blesses for Card A3: "time a fixed number of training updates for
throughput only; do not run audit validation or test, and do not use it to set
anything".

THIS IS NOT A FIT. No model is trained to completion, nothing is selected, no
checkpoint is kept, and nothing here feeds any later choice. It does not consume
the two permitted development fits.

Usage: python -I 07_2d_throughput_probe.py <out_dir> <cache_dir> [threads] [updates]
"""
import json
import os
import sys
import time

import numpy as np
import pandas as pd
import torch
import torch.nn as nn

OUT = os.path.abspath(sys.argv[1])
CACHE = os.path.abspath(sys.argv[2])
THREADS = int(sys.argv[3]) if len(sys.argv) > 3 else 6
N_UPDATES = int(sys.argv[4]) if len(sys.argv) > 4 else 20

SEED = 22
BATCH = 128
NPERSEG, NOVERLAP = 64, 48

torch.manual_seed(SEED)
np.random.seed(SEED)
torch.set_num_threads(THREADS)

ids = pd.read_csv(os.path.join(OUT, "I2_official_split_ids.csv"), index_col="ecg_id")
sig = np.load(os.path.join(CACHE, "signals_lr_f32.npy"), mmap_mode="r")
part = ids["partition"].values
n_train = int((part == "train").sum())

window = torch.hann_window(NPERSEG)


def spectrograms(x):
    """x: (n, 12, 1000) float32 tensor -> log-power STFT, (n, 12, F, T)."""
    n, c, t = x.shape
    z = torch.stft(x.reshape(n * c, t), n_fft=NPERSEG, hop_length=NPERSEG - NOVERLAP,
                   win_length=NPERSEG, window=window, return_complex=True, center=True)
    p = torch.log1p(z.abs() ** 2)
    return p.reshape(n, c, p.shape[-2], p.shape[-1])


# ---- cost of the time-frequency transform itself (preprocessing, per 1000 records)
probe = torch.from_numpy(np.ascontiguousarray(sig[:1000]))
t0 = time.time()
S = spectrograms(probe)
stft_seconds_per_1000 = time.time() - t0
print("spectrogram tensor per batch of 1000: %s" % (tuple(S.shape),))
print("STFT cost: %.2fs per 1000 records" % stft_seconds_per_1000)

F, T = S.shape[2], S.shape[3]


class ECG2DCNN(nn.Module):
    """2-D CNN over per-lead spectrograms stacked as channels (12 input channels)."""

    def __init__(self, c_in=12, n_out=5):
        super().__init__()

        def block(ci, co):
            return nn.Sequential(nn.Conv2d(ci, co, 3, padding=1, bias=False),
                                 nn.BatchNorm2d(co), nn.ReLU(inplace=True), nn.MaxPool2d(2))

        self.features = nn.Sequential(block(c_in, 32), block(32, 64), block(64, 96))
        self.head = nn.Sequential(nn.AdaptiveAvgPool2d(1), nn.Flatten(),
                                  nn.Dropout(0.3), nn.Linear(96, n_out))

    def forward(self, x):
        return self.head(self.features(x))


model = ECG2DCNN()
n_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
assert n_params <= 250_000, n_params
opt = torch.optim.Adam(model.parameters(), lr=1e-3)
lossf = nn.BCEWithLogitsLoss()

xb = S[:BATCH]
yb = torch.zeros(BATCH, 5)          # shape-only; no label is read for a throughput probe

model.train()
for _ in range(3):                  # warm-up, excluded from the timing
    opt.zero_grad(set_to_none=True)
    lossf(model(xb), yb).backward()
    opt.step()

t0 = time.time()
for _ in range(N_UPDATES):
    opt.zero_grad(set_to_none=True)
    lossf(model(xb), yb).backward()
    opt.step()
elapsed = time.time() - t0

per_update = elapsed / N_UPDATES
updates_per_epoch = int(np.ceil(n_train / BATCH))
epoch_seconds = per_update * updates_per_epoch

report = {
    "purpose": "throughput only, for the 24-hour programme projection; not a fit",
    "spectrogram_shape_per_record": [12, int(F), int(T)],
    "stft_nperseg": NPERSEG, "stft_noverlap": NOVERLAP,
    "stft_seconds_per_1000_records": round(stft_seconds_per_1000, 2),
    "stft_seconds_all_21375_records": round(stft_seconds_per_1000 * 21.375, 1),
    "trainable_parameters": n_params, "d0_parameter_cap": 250000,
    "threads": THREADS, "batch_size": BATCH,
    "updates_timed": N_UPDATES,
    "seconds_per_update": round(per_update, 4),
    "updates_per_epoch": updates_per_epoch,
    "projected_epoch_seconds": round(epoch_seconds, 1),
    "projected_30_epoch_seconds": round(epoch_seconds * 30, 1),
    "note": "No checkpoint kept, no selection made, no test data or label touched.",
}
with open(os.path.join(OUT, "I2_2d_throughput_probe.json"), "w", encoding="utf-8") as fh:
    json.dump(report, fh, indent=2)

print("2-D CNN trainable params : %d (cap 250000)" % n_params)
print("timed %d updates in %.2fs -> %.3f s/update" % (N_UPDATES, elapsed, per_update))
print("projected epoch (%d updates) : %.0f s" % (updates_per_epoch, epoch_seconds))
print("projected 30 epochs          : %.0f s (%.1f min)" % (epoch_seconds * 30, epoch_seconds * 30 / 60))
print("-> the 30-minute per-fit cap binds first" if epoch_seconds * 30 > 1800
      else "-> 30 epochs fit inside the 30-minute cap")
