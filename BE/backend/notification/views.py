from django.shortcuts import render
from django.conf import settings
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

import boto3

from .serializers import NotificationSerializer
from .models import Notification

def get_s3object():
  s3 = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY,
        region_name = settings.AWS_REGION
      )
      
  obj_list = s3.list_objects(Bucket=settings.AWS_STORAGE_BUCKET_NAME)
  contents_list = obj_list['Contents']
  return contents_list


def save_notification():
  contents_list = get_s3object()

  data = {}

  for content in contents_list:
    key = content['Key']
    if ('/' not in key):
      continue

    data['target_center'], data['title'] = key.split('/')
    data['content'] = 'https://' + settings.AWS_S3_CUSTOM_DOMAIN + '/' + key
  
    serializer = NotificationSerializer(data=data)
    if serializer.is_valid():
        serializer.save()

class NotificationView(APIView):
    def get(self, request, id):
        notifications = get_object_or_404(Notification, id = id)
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)