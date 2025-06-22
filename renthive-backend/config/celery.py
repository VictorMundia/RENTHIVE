from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
# Ensures compatibility with Python 2 and 3, making imports absolute and strings Unicode by default.
# Imports the operating system module, providing a way to interact with the OS.
# Imports the Celery class from the celery library.
# Sets the default Django settings module for the 'celery' program.
# Creates a Celery application instance named 'config'.
# Loads Celery configuration from Django settings, using 'CELERY' as the namespace for Celery-specific settings.
# Automatically discovers tasks in installed Django apps.
