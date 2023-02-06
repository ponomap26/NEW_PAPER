import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'New_Portal.settings')

app = Celery('New_Portal')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.timezone = 'Europe/Moscow'

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'post_ my_job_post_8am': {
        'task': 'news.tasks.my_job',
        'schedule': crontab(hour=8, minute=00, day_of_week='monday'),

    },
}


