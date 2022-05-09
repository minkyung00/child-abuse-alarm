from __future__ import absolute_import, unicode_literals
from celery import shared_task

from .capstone import main

@shared_task
def func():
    main.upload_video()