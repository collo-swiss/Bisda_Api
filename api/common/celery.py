from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab

import django
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.config.local')
django.setup()

from api.audits.tasks import compose_survey

app = Celery('mammoth-api')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.timezone = 'Africa/Nairobi'

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):

    sender.add_periodic_task(
        crontab(minute=0, hour='6,9,12,15'),
        compose_survey.s(), name='send out audits according to their frequency'
    )