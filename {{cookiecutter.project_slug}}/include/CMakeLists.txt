# in include
# include_directories(clrprint)

# installation
install(FILES {{ cookiecutter.project_slug }}/{{ cookiecutter.project_slug }}.h
  DESTINATION include/{{ cookiecutter.project_slug }}
)
