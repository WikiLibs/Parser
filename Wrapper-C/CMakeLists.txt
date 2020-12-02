cmake_minimum_required(VERSION 3.10)

# set the project name
project(Tutorial)


# find the executable and store in var
file(GLOB MyBins
  Linux/mybin.*.c
)

# add the executable
set(MAIN Linux/exec.c)
add_executable(Tutorial ${MyBins} ${MAIN})

# add the binary tree to the search path for include files
# so that we will find the headers file
configure_file(Linux/exec.c Linux/mybin.h)
include_directories("${CMAKE_SOURCE_DIR}/Linux")

# specify the C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)
