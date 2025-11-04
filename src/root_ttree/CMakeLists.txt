find_package(ROOT REQUIRED COMPONENTS RIO Tree Hist)
include(${ROOT_USE_FILE})
add_executable(ttree_demo ttree_demo.cpp)
target_link_libraries(ttree_demo ${ROOT_LIBRARIES})

