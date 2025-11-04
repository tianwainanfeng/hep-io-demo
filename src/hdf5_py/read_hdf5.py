# read_hdf5.py
import h5py
import numpy as np
with h5py.File("data/demo.h5","r") as f:
    dset = f["events/px"]
    print("shape:", dset.shape, "dtype:", dset.dtype)
    # read first 10 rows
    print(dset[:10])

