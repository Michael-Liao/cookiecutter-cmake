# TOP
cmake_minimum_required(VERSION 3.0)

#project name
project({{ cookiecutter.project_slug }})
subdirs(include src test)

IF(CMAKE_BUILD_TYPE STREQUAL Debug)
  add_definitions(-DPRINT_DEBUG_MSG)
ENDIF()

# catch needs c++11
SET(CMAKE_CXX_STANDARD 11)

# uncomment to run tests with CTest
# enable_testing(TRUE)
# add_test(NAME FirstTest COMMAND test/{{ cookiecutter.project_slug.upper() }})
