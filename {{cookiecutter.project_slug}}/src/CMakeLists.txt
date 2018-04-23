# in src
# path of headers
include_directories(${PROJECT_SOURCE_DIR}/include/{{ cookiecutter.project_slug }})
# include_directories(${PROJECT_SOURCE_DIR}/include) # doesn't work
add_executable({{ cookiecutter.project_slug }} main.cpp)
add_library({{ cookiecutter.project_slug }} {{ cookiecutter.project_slug }}.cpp)
target_link_libraries({{ cookiecutter.project_slug }} {{ cookiecutter.project_slug }})

# installation
install(TARGETS {{ cookiecutter.project_slug }} DESTINATION bin)
