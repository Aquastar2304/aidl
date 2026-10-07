#!/usr/bin/env python3
"""Card I4-S / Annex D8 reference implementation, issued with the cards (24 September 2026, revised 25 September:
input paths are now arguments; the algorithm and its output are unchanged).
Usage: python i4s_grouping_and_split.py TAU OUTDIR SEAMS POS STATS
  SEAMS  little-endian float32, (N+1) x 4 x 128: band-14 left column, right column, top row, bottom row of each
         patch image_<id>.h5 (id 1..3799; slot 0 unused)
  POS    little-endian int32, N+1: landslide pixels per patch (mask value 1)
  STATS  little-endian float32, (N+1) x 4: band-14 min, band-14 max, slope (band 13) max, band-14 range
The three inputs are written by i4s_extract_seams.py from the pinned mirror's patches (default names below).
Rule (D8): seam distance = max |difference| over 128 pixels. A seam is informative if max-min >= 0.01.
A horizontal link i->j (right edge of i to left edge of j) is kept iff BOTH seams are informative, d < tau, j is
i's nearest informative left edge AND i is j's nearest informative right edge (reciprocal nearest neighbours);
exact ties go to the lower patch ID. Vertical links (bottom of i to top of j) likewise. Groups = connected
components over both directions. An unlinked patch joins the group of its lower index neighbour, taken in
ascending ID order, unless the very next ID is linked into a different group (then it is left unassigned).
Coordinates come from ID arithmetic at each group's dominant vertical stride; the link walk is a check.
Degenerate = band-14 min equals max and slope statistic zero; degenerate patches are grouped, then excluded.
"""
import numpy as np, csv, collections, hashlib, sys, os
N=3799; TAU=float(sys.argv[1]) if len(sys.argv)>1 else 0.05; OUT=sys.argv[2] if len(sys.argv)>2 and sys.argv[2]!="-" else None
SEAMS,POS,STATS=(sys.argv[3:6] if len(sys.argv)>5 else ["seams.bin","pos.bin","stats.bin"])
e=np.fromfile(SEAMS,dtype="<f4").reshape(-1,4,128)
L,R,T,B=(np.ascontiguousarray(e[1:N+1,k,:]) for k in range(4))
pos=np.fromfile(POS,dtype="<i4")[1:N+1]
st=np.fromfile(STATS,dtype="<f4").reshape(-1,4)[1:N+1]   # per patch: band-14 min, band-14 max, two slope statistics
deg=(st[:,0]==st[:,1])&(st[:,2]==0)          # band 14 constant and slope identically zero: 114 patches
inf=lambda A:(A.max(1)-A.min(1))>=0.01
okL,okR,okT,okB=inf(L),inf(R),inf(T),inf(B)
def nn(A,okA,Bm,okBm):
    bj=np.full(len(A),-1,np.int64); bd=np.full(len(A),np.inf)
    cand=np.where(okBm)[0]; Bc=Bm[cand]
    for s in range(0,len(A),48):
        f=min(s+48,len(A)); d=np.abs(A[s:f,None,:]-Bc[None,:,:]).max(2).astype(np.float64)
        d[cand[None,:]==np.arange(s,f)[:,None]]=np.inf
        k=d.argmin(1)                      # argmin returns the first minimum = lowest candidate ID
        bj[s:f]=cand[k]; bd[s:f]=d[np.arange(f-s),k]
    bj[~okA]=-1; bd[~okA]=np.inf
    return bj,bd
rj,rd=nn(R,okR,L,okL); lj,ld=nn(L,okL,R,okR)      # right->left, left->right
bj,bdd=nn(B,okB,T,okT); tj,td=nn(T,okT,B,okB)      # bottom->top, top->bottom
H=[(i,int(rj[i])) for i in range(N) if rj[i]>=0 and rd[i]<TAU and lj[rj[i]]==i]
V=[(i,int(bj[i])) for i in range(N) if bj[i]>=0 and bdd[i]<TAU and tj[bj[i]]==i]
p=list(range(N))
def f(a):
    while p[a]!=a: p[a]=p[p[a]]; a=p[a]
    return a
for a,b in H+V:
    ra,rb=f(a),f(b)
    if ra!=rb: p[max(ra,rb)]=min(ra,rb)
root=np.array([f(i) for i in range(N)]); size=collections.Counter(root)
grp=root.copy(); attached=[]; unassigned=[]; linked=lambda k: size[root[k]]>1
for i in range(N):                      # ascending ID: tiles were written in scan order
    if linked(i): continue
    lower=grp[i-1] if i>0 and (i-1) not in unassigned else None
    nxt=next((k for k in range(i+1,N) if linked(k)),None); upper=grp[nxt] if nxt is not None else None
    if lower is not None and size[root[i-1]]>1 or (i-1) in attached:
        if nxt==i+1 and upper!=lower: unassigned.append(i)      # the next tile already opens a different scene
        else: grp[i]=lower; attached.append(i)
    else: unassigned.append(i)
big=sorted([g for g in set(grp[i] for i in range(N) if i not in unassigned)],key=lambda g:g)
names={g:f"S{k+1}" for k,g in enumerate(sorted(big,key=lambda g:min(np.where(grp==g)[0])))}
stride={}
for g in big:
    c=collections.Counter(b-a for a,b in V if grp[a]==g and grp[b]==g); stride[g]=c.most_common(1)[0][0] if c else None
# walk links
coord={}; conflicts=[]
adj=collections.defaultdict(list)
for a,b in H: adj[a].append((b,1,0)); adj[b].append((a,-1,0))
for a,b in V: adj[a].append((b,0,1)); adj[b].append((a,0,-1))
for g in big:
    s=min(i for i in range(N) if grp[i]==g and i not in attached); coord[s]=(0,0); st=[s]
    while st:
        u=st.pop()
        for v,dx,dy in adj[u]:
            c=(coord[u][0]+dx,coord[u][1]+dy)
            if v in coord:
                if coord[v]!=c: conflicts.append((u+1,v+1,coord[v],c))
            else: coord[v]=c; st.append(v)
arith_mismatch=0
for g in big:
    first=min(np.where(grp==g)[0])
    for i in np.where(grp==g)[0]:
        c=((i-first)%stride[g],(i-first)//stride[g])
        if i in attached or i not in coord: coord[i]=c
        elif coord[i]!=c: arith_mismatch+=1
# shift walked coordinates to the group's origin (the walk starts at the lowest ID, which is (0,0))
print(f"tau {TAU}: links h {len(H)} v {len(V)}; components with >1 patch {len(big)}; attached {len(attached)}; unassigned {[u+1 for u in unassigned]}")
print("link-walk conflicts",len(conflicts),conflicts[:3],"; walked coords that differ from index arithmetic",arith_mismatch)
for g in sorted(big,key=lambda g:names[g]):
    ids=np.where(grp==g)[0]; w=stride[g]; nr=(ids.max()-ids.min())//w+1
    print(names[g],"patches",len(ids),"ids %d-%d"%(ids.min()+1,ids.max()+1),"contiguous",ids.max()-ids.min()+1==len(ids),"stride",w,"grid %dx%d"%(w,nr),
          "pos",int((pos[ids]>0).sum()),"neg",int((pos[ids]==0).sum()),"degenerate",int(deg[ids].sum()))
if OUT is None: sys.exit()
# roles
S1=[g for g in big if names[g]=='S1'][0]
rows=[]
for i in range(N):
    g=None if i in unassigned else grp[i]; sg=names.get(g,'UNASSIGNED')
    c=coord.get(i,('','')); role=None
    if deg[i]: role='excluded_degenerate'
    elif sg=='S1':
        col=c[0]; role='S1_train' if col<=22 else 'S1_guard' if col in (23,31) else 'S1_val' if col<=30 else 'S1_test'
    elif sg=='UNASSIGNED': role='excluded_unassigned'
    else: role='transfer_pool'
    rows.append(dict(patch_id=i+1,scene_group=sg,grid_col=c[0],grid_row=c[1],is_positive=int(pos[i]>0),n_landslide_pixels=int(pos[i]),degenerate=int(deg[i]),role=role))
cnt=collections.Counter((r['role'],r['is_positive']) for r in rows)
for role in ['S1_train','S1_val','S1_test','S1_guard','transfer_pool','excluded_degenerate']:
    print(role,cnt[(role,1)]+cnt[(role,0)],"(%d pos / %d neg)"%(cnt[(role,1)],cnt[(role,0)]))
os.makedirs(OUT,exist_ok=True)
def w(fn,fields,rs):
    with open(os.path.join(OUT,fn),'w',newline='') as fh:
        wr=csv.DictWriter(fh,fieldnames=fields,lineterminator='\n'); wr.writeheader(); [wr.writerow(r) for r in rs]
    print(fn,hashlib.sha256(open(os.path.join(OUT,fn),'rb').read()).hexdigest())
w("Landslide4Sense_I4S_split.csv",list(rows[0].keys()),rows)
w("Landslide4Sense_scene_groups.csv",['patch_id','scene_group','n_landslide_pixels','is_positive'],[{k:r[k] for k in ['patch_id','scene_group','n_landslide_pixels','is_positive']} for r in rows])
summ=[]
for g in sorted(big,key=lambda g:names[g]):
    ids=np.where(grp==g)[0]
    summ.append(dict(scene_group=names[g],n_patches=len(ids),n_positive_patches=int((pos[ids]>0).sum()),n_negative_patches=int((pos[ids]==0).sum()),
        total_landslide_pixels=int(pos[ids].sum()),min_patch_id=ids.min()+1,max_patch_id=ids.max()+1,vertical_raster_stride=stride[g],fold_eligible=1))
for u in unassigned: summ.append(dict(scene_group='UNASSIGNED',n_patches=1,n_positive_patches=int(pos[u]>0),n_negative_patches=int(pos[u]==0),total_landslide_pixels=int(pos[u]),min_patch_id=u+1,max_patch_id=u+1,vertical_raster_stride='',fold_eligible=0))
w("Landslide4Sense_scene_group_summary.csv",list(summ[0].keys()),summ)
ts=collections.Counter((r['scene_group'],r['is_positive']) for r in rows if not r['degenerate'])
tst=cnt[('S1_test',1)]+cnt[('S1_test',0)]
folds=[dict(fold='F1-S1',test_set='S1 guarded test block',transfer_train_groups='S2+S4',transfer_val_group='S3',n_test=tst,n_test_pos=cnt[('S1_test',1)],n_test_neg=cnt[('S1_test',0)])]
for fo,g,tr,va in [('F2-S2','S2','S1+S4','S3'),('F3-S3','S3','S1+S2','S4'),('F4-S4','S4','S1+S3','S2')]:
    folds.append(dict(fold=fo,test_set='all of '+g,transfer_train_groups=tr,transfer_val_group=va,n_test=ts[(g,1)]+ts[(g,0)],n_test_pos=ts[(g,1)],n_test_neg=ts[(g,0)]))
w("Landslide4Sense_I4S_folds.csv",list(folds[0].keys()),folds)
