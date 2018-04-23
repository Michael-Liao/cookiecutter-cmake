# in test
# single file library setup
add_library(Catch INTERFACE)
target_include_directories(Catch INTERFACE ${PROJECT_SOURCE_DIR}/include)

# add this so we can do `make catch`
add_custom_target(catch
  COMMAND {{ cookiecutter.project_slug.upper() }}_test
  COMMENT "running catch defined tests"
)

add_executable({{ cookiecutter.project_slug.upper() }}
  test-main.cpp
  test-{{ cookiecutter.project_slug }}.cpp
  ${PROJECT_SOURCE_DIR}/src/{{ cookiecutter.project_slug }}.cpp
)
target_link_libraries({{ cookiecutter.project_slug.upper() }} Catch)
