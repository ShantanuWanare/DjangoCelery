from __future__ import absolute_import, unicode_literals
import os 
from celery import Celery 
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangocelery.settings')

app = Celery('djangocelery')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')

# Celery beat settings
app.conf.beat_schedule = {
    'send-mail-every-day-at-8':{
        'task': 'mailapp.tasks.send_mail_func',
        'schedule' : crontab(hour=11, minute=36) # day_of_month = 20 , month_of_year = 6
        # 'args' : (2,)  can pass args from here to send_mail_func

    }

}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')