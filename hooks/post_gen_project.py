#!/usr/bin/env python
import os
# import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

# def remove_dir(dirpath):
    # shutil.rmtree(os.path.join(PROJECT_DIRECTORY, dirpath))

def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':
    if '{{ cookiecutter.use_catch }}' != 'y':
        pass
        # remove_file('vendor/catch/catch.hpp')
    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        pass
        # remove_file('include/clara.hpp')

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE.md')
