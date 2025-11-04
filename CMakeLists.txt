cmake_minimum_required(VERSION 3.15)
project(hep-io-demo LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
add_subdirectory(src/root_ttree)
add_subdirectory(src/root_rntuple)
# Python examples don't need CMake; keep them in src/hdf5_py and call from scripts
