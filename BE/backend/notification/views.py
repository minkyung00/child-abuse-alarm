from django.shortcuts import render
from django.conf import settings
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

import boto3
import datetime
from django.utils import timezone

from .serializers import NotificationSerializer, NotificationWeeklySerializer
from .models import Notification, NotificationWeekly
from center.models import Center

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


def save_notification(target_center, content):
  data = {}

  key = 'video/' + target_center + ',' + content + '.mp4'
  
  video_index = content.split(',')[0]
  act = content.split(',')[1]

  hit_cnt = kick_cnt = 0
  if (act == 'hit'):
      hit_cnt = content.split(',')[2]
  elif (act == 'kick'):
      kick_cnt = content.split(',')[2]
  else:
      hit_cnt = content.split(',')[2]
      kick_cnt = content.split(',')[3]

  data['title'] = video_index + ',' + act
  data['content'] = settings.AWS_S3_CUSTOM_DOMAIN + '/' + key
  data['target_center'] = Center.objects.get(name=target_center)
  data['hit_count'] = int(hit_cnt)
  data['kick_count'] = int(kick_cnt)

  total_count = int(hit_cnt) + int(kick_cnt)
  if (total_count >= 5):
      data['status'] = 'danger'
  elif (total_count >= 2):
      data['status'] = 'warning'
  elif (total_count > 0):
      data['status'] = 'caution'

  serializer = NotificationSerializer(data=data)
  if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)

class NotificationView(APIView):
    def get(self, request, id):
        notifications = get_object_or_404(Notification, id = id)
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class NotificationWeeklyView(APIView):
    def get_weeklylist(self):
        start_date = datetime.datetime.strftime((timezone.now() - datetime.timedelta(weeks=1)), '%Y-%m-%d')
        end_date = timezone.now()
        week = Notification.objects.filter(created_time__range=(start_date, end_date))

        if week.exists():
            return week, start_date
        else:
            return None, None

    def get(self, request):
        weekly_list, start_date = self.get_weeklylist()

        if weekly_list is None:
            return Response({"error": "이번주 알림 내역이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

        total_hit = total_kick = total_danger = total_warning = total_caution = 0
        for day in weekly_list:
            total_hit += day.hit_count
            total_kick += day.kick_count
            if (day.status == 'danger'):
                total_danger += 1
            if (day.status == 'warning'):
                total_warning += 1
            if (day.status == 'caution'):
                total_caution += 1
        
        data = {
            "start_date": start_date,
            "total_hit": total_hit,
            "total_kick": total_kick,
            "total_danger": total_danger,
            "total_warning": total_warning,
            "total_caution": total_caution,
        }

        # 폭력행위가 감지되지 않았을 경우 -> 기존의 데이터 전송
        try:
            weekly = NotificationWeekly.objects.get(start_date=start_date, total_hit=total_hit, total_kick=total_kick, total_danger=total_danger, total_warning=total_warning, total_caution=total_caution)
            return Response(data, status=status.HTTP_200_OK)

        # 폭력행위가 감지된 경우 -> 새로 저장
        except NotificationWeekly.DoesNotExist:
            serializer = NotificationWeeklySerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(data, status=status.HTTP_200_OK)
          