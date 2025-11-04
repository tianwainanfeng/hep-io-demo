# write_hdf5.py
import h5py, numpy as np
import os

os.makedirs("data", exist_ok=True)
with h5py.File("data/demo.h5", "w") as f:
    grp = f.create_group("events")
    # create chunked, compressed dataset for px (variable-length per event -> store as ragged)
    # Simple approach: store fixed-length arrays or use variable-length via special dtype
    dset = grp.create_dataset("px", (1000,5), maxshape=(None,5),
                              dtype='f4', chunks=(100,5), compression="gzip", compression_opts=4)
    # fill with synthetic values (pad with NaN)
    for i in range(1000):
        row = np.full(5, np.nan, dtype=np.float32)
        n = (i % 5) + 1
        row[:n] = np.random.normal(size=n)
        dset[i] = row
print("Wrote data/demo.h5")

