#!/usr/bin/env bash

# install requirements
pip install -r requirements.txt

# start celery worker
celery -A site_html_elements_getter worker --loglevel=INFO --detach


# run server
python manage.py runserver

