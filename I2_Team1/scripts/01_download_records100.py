"""
22AIE304 / Card I2 (Team 1) - Step 9 acquisition.

Downloads ONLY the approved required subset named on Card I2:
PTB-XL v1.0.3 `records100` (plus the metadata files already fetched).

Source: AWS Open Data mirror of PhysioNet, s3://physionet-open/ptb-xl/1.0.3/
served over HTTPS (no credentials, no login). Manifest I2 records this
mirror as serving the same bytes as physionet.org and being far faster.

Integrity: every file is verified against the project's own SHA256SUMS.txt.

Usage:  python -I 01_download_records100.py <dataset_root> [workers]
"""
import hashlib
import os
import sys
import threading
import time
import urllib.request

BASE = "https://physionet-open.s3.amazonaws.com/ptb-xl/1.0.3/"
ROOT = os.path.abspath(sys.argv[1])
WORKERS = int(sys.argv[2]) if len(sys.argv) > 2 else 16

sums_path = os.path.join(ROOT, "SHA256SUMS.txt")
targets = []
with open(sums_path, "r", encoding="utf-8") as fh:
    for line in fh:
        line = line.rstrip("\n")
        if not line:
            continue
        digest, _, rel = line.partition(" ")
        rel = rel.strip()
        if rel.startswith("records100/"):
            targets.append((rel, digest))

print(f"records100 files listed in SHA256SUMS.txt: {len(targets)}", flush=True)

lock = threading.Lock()
state = {"done": 0, "bytes": 0, "ok": 0, "bad": [], "fail": []}
t0 = time.time()


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def fetch(item):
    rel, digest = item
    dest = os.path.join(ROOT, rel.replace("/", os.sep))
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    transferred = 0
    if os.path.exists(dest) and sha256_file(dest) == digest:
        status = "cached"
    else:
        last_err = None
        status = None
        for attempt in range(4):
            try:
                req = urllib.request.Request(BASE + rel, headers={"User-Agent": "22AIE304-I2/1.0"})
                with urllib.request.urlopen(req, timeout=60) as resp:
                    data = resp.read()
                transferred = len(data)
                with open(dest, "wb") as fh:
                    fh.write(data)
                status = "ok" if hashlib.sha256(data).hexdigest() == digest else "badhash"
                break
            except Exception as exc:  # noqa: BLE001
                last_err = exc
                time.sleep(1.5 * (attempt + 1))
        if status is None:
            status = f"fail:{last_err}"
    with lock:
        state["done"] += 1
        state["bytes"] += transferred
        if status in ("ok", "cached"):
            state["ok"] += 1
        elif status == "badhash":
            state["bad"].append(rel)
        else:
            state["fail"].append((rel, status))
        if state["done"] % 2000 == 0:
            el = time.time() - t0
            print(f"  {state['done']}/{len(targets)}  {state['bytes']/1e6:.1f} MB  {el:.0f}s", flush=True)


def main():
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        list(pool.map(fetch, targets))
    el = time.time() - t0
    print(f"\nfiles verified OK : {state['ok']}/{len(targets)}")
    print(f"hash mismatches   : {len(state['bad'])} {state['bad'][:10]}")
    print(f"failed downloads  : {len(state['fail'])} {state['fail'][:5]}")
    print(f"bytes transferred this run : {state['bytes']}")
    print(f"elapsed                    : {el:.1f}s")


if __name__ == "__main__":
    main()
