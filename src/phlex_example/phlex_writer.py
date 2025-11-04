# simple phlex-style adapter that writes Layer/Cell/Family as groups/attrs in HDF5
import h5py, numpy as np, os
os.makedirs("data", exist_ok=True)

with h5py.File("data/phlex_demo.h5","w") as f:
    # top-level layer
    layer = f.create_group("layer_event")
    # set metadata for provenance
    layer.attrs['phlex_version'] = "0.3"
    layer.attrs['producer'] = "demo_phlex_writer"

    # create a family that groups cells
    family = layer.create_group("family_0001")
    for cell_idx in range(10):
        cell = family.create_group(f"cell_{cell_idx:04d}")
        # store cell-level attributes
        cell.attrs['run'] = 1
        cell.attrs['cell_index'] = cell_idx
        # store a dataset (e.g., px for events in that cell)
        data = np.random.normal(size=(100,))  # small example
        cell.create_dataset("px", data=data, compression="gzip")
print("Wrote data/phlex_demo.h5 (Phlex-style layout)")

