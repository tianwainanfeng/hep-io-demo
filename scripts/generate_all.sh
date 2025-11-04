#!/usr/bin/env bash
set -e
mkdir -p data
# Run ROOT TTree (C++ binary)
./build/src/root_ttree/ttree_demo
# Run RNTuple demo (if built)
./build/src/root_rntuple/rntuple_demo || echo "RNTuple demo failed or not built"
# Run HDF5 python demo
python src/hdf5_py/write_hdf5.py
python src/hdf5_py/read_hdf5.py
# Run Phlex adapter
python src/phlex_example/phlex_writer.py
ls -lh data

