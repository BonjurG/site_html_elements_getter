import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'site_html_elements_getter.settings')
app = Celery('site_html_elements_getter')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
