#!/usr/bin/env bash

#celery -A site_html_elements_getter worker -l info
# install requirements
pip install -r requirements.txt

# run server
python manage.py runserver

