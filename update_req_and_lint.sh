#!/usr/bin/env bash
# update requirements file
pip freeze > requirements.txt

# do linting stuff
pep8 site_html_elements_getter
pylint site_html_elements_getter

