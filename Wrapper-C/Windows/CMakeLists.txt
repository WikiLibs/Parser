cmake_minimum_required(VERSION 3.10)

# set the project name
project(Wrapper_Windows)

# find the executable and store in var
file(GLOB MyBins
  mybins/mybin.*
  )

file(GLOB Constants
  code/constant.*
  )


# add the executable
set(MAIN ${CMAKE_CURRENT_SOURCE_DIR}/code/CreatePross.cpp)
add_executable(Wrapper_Linux ${MyBins} ${Constants} ${MAIN})

# add the binary tree to the search path for include files
# so that we will find the headers file
include_directories("${CMAKE_CURRENT_SOURCE_DIR}/mybins" "${CMAKE_CURRENT_SOURCE_DIR}/code")

# specify the C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)
