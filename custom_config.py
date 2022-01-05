#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function
from cookiecutter.main import cookiecutter
from yaml import load, YAMLError, FullLoader


try:
    with open('demofile.txt', 'r') as file:
        from_file = file.read()
except YAMLError as exc:
    print("Error in configuration file: %s" % exc)


CONFIGURATIONS = {
    "project_name": "my_project",
    "from_file": from_file
}

cookiecutter('template', no_input=True,
             overwrite_if_exists=True, extra_context=CONFIGURATIONS)