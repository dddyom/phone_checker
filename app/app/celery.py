import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

app = Celery("app")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

app.conf.beat_schedule = {
    "load_numeric_registry": {
        "task": "phone_checker.tasks.load_numeric_registry",
        "schedule": crontab(hour="0", minute="0"),
    },
}
