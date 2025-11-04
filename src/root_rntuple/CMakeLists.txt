cmake_minimum_required(VERSION 3.16)
project(root_rntuple_demo LANGUAGES CXX)

# Find ROOT (requires ROOT to be installed with RNTuple support)
#find_package(ROOT REQUIRED COMPONENTS RNTuple)
#find_package(ROOT REQUIRED COMPONENTS Tree RIO)
find_package(ROOT QUIET)
if (NOT ROOT_FOUND OR NOT EXISTS "${ROOT_INCLUDE_DIRS}/ROOT/RNTuple.hxx")
    message(WARNING "RNTuple headers not found, skipping RNTuple demo build.")
    return()
endif()

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Source files
set(SOURCES
    rntuple_demo.cpp
)

# Create executable
add_executable(rntuple_demo ${SOURCES})

# Link to ROOT libraries
#target_link_libraries(rntuple_demo PRIVATE ROOT::RNTuple)

# Optionally include ROOT headers automatically
target_include_directories(rntuple_demo PRIVATE ${ROOT_INCLUDE_DIRS})

# Optional: install the binary
install(TARGETS rntuple_demo
        RUNTIME DESTINATION bin)

