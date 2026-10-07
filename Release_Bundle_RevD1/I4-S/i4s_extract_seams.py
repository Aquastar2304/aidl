#!/usr/bin/env python3
"""Card I4-S / Annex D8: build the three inputs of i4s_grouping_and_split.py from the Landslide4Sense patches.
Issued with the cards, 25 September 2026.

Usage: python i4s_extract_seams.py IMG_DIR MASK_DIR OUT_DIR
  IMG_DIR   folder holding image_1.h5 ... image_3799.h5 (mirror path images/train/)
  MASK_DIR  folder holding mask_1.h5 ... mask_3799.h5  (mirror path annotations/train/; ignore the five
            800-byte strays named image_*.h5 in that folder)
Reads each file as HDF5 data at byte offset 2048: images float64 128 x 128 x 14 (band last), masks uint8 128 x 128.
Writes, with slot 0 unused and patch id p in slot p (N = 3799):
  seams.bin  little-endian float32, (N+1) x 4 x 128 - band 14 (index 13) as float32:
             left column [:,0], right column [:,127], top row [0,:], bottom row [127,:]
  pos.bin    little-endian int32, N+1 - number of mask pixels equal to 1
  stats.bin  little-endian float32, (N+1) x 4 - band-14 min, band-14 max, slope (band 13, index 12) max,
             band-14 range (max - min, computed in float64, then stored as float32)
A patch is degenerate when band-14 min equals max and slope max is 0 (114 patches).
Checked against the instructor's files on 8 patches (1, 2, 42, 2460, 2500, 3034, 3035, 3799): identical bytes.
Reads the files one at a time; peak memory is one patch.
"""
import numpy as np, os, sys
N=3799
img,msk,out=sys.argv[1:4]
seams=np.zeros((N+1,4,128),"<f4"); pos=np.zeros(N+1,"<i4"); st=np.zeros((N+1,4),"<f4")
for p in range(1,N+1):
    x=np.frombuffer(open(os.path.join(img,f"image_{p}.h5"),"rb").read()[2048:],"<f8").reshape(128,128,14)
    m=np.frombuffer(open(os.path.join(msk,f"mask_{p}.h5"),"rb").read()[2048:],np.uint8).reshape(128,128)
    b=x[:,:,13]; s=x[:,:,12]                     # float64 as stored
    seams[p]=np.stack([b[:,0],b[:,127],b[0,:],b[127,:]]).astype("<f4")
    pos[p]=int((m==1).sum())
    st[p]=np.array([b.min(),b.max(),s.max(),b.max()-b.min()],"<f8").astype("<f4")   # range taken in float64
os.makedirs(out,exist_ok=True)
seams.tofile(os.path.join(out,"seams.bin")); pos.tofile(os.path.join(out,"pos.bin")); st.tofile(os.path.join(out,"stats.bin"))
print("patches",N,"positive",int((pos[1:]>0).sum()),"degenerate",int(((st[1:,0]==st[1:,1])&(st[1:,2]==0)).sum()))
