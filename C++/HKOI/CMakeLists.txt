cmake_minimum_required(VERSION 3.0.0)
project(HKOI VERSION 0.1.0)

include(CTest)
enable_testing()

# no need to be complex for this project
add_executable(HKOI main.cpp
               s191/unstoppable_onslaught.h s191/unstoppable_onslaught.cpp)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
