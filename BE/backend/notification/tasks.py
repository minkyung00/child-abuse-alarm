from __future__ import absolute_import, unicode_literals
from celery import shared_task

@shared_task
def task_upload_video():
    from .capstone_new.main import upload_video
    import boto3
    from django.conf import settings
    s3 = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY,
            region_name = settings.AWS_REGION
        )
    
    upload_video()
