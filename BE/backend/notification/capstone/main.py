from . import yolo
import boto3
import os
import shutil
import urllib.request
from urllib.error import HTTPError

from django.conf import settings

# for i in range(1, 100):
#     s3.upload_file('tmp_data/'+str(i)+'.jpg', bucket_name, str(i)+'.jpg')

s3 = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY,
        region_name = settings.AWS_REGION
      )

# 없는 url이면 True 반환
def is_not_valid_url(index):
    url = 'https://capstone1234.s3.ap-northeast-2.amazonaws.com/' + str(index) + '.jpg'
    try:
        resp = urllib.request.urlopen(url)
    except HTTPError as e:
        return True
    return False

def make_video(key_list, video_index, hit_flag, kick_flag):
    for i in range(key_list[0]-10, key_list[-1]+10):
        if i <= 0 or i in key_list:
            continue
        key_list.append(i)
    key_list.sort()
    # test 폴더 없으면 만들기
    if not os.path.isdir('test'):
        os.mkdir('test')

    # s3에서 img 받아오기
    for i in key_list:
        if is_not_valid_url(i):
            continue
        s3.download_file(settings.AWS_STORAGE_BUCKET_NAME, str(i) + '.jpg', 'test/' + str(i) + '.jpg')

    # 동영상 만들기
    os.system(f'ffmpeg -r 5 -pattern_type glob -i "test/*.jpg"'
              f' -crf 20 test/test.mp4')

    # 동영상 s3에 업로드
    if hit_flag == 1 and kick_flag == 0:
        s3.upload_file('test/test.mp4', settings.AWS_STORAGE_BUCKET_NAME, 'video/천호어린이집,' + str(video_index) + ',hit' + '.mp4')
    elif hit_flag == 0 and kick_flag == 1:
        s3.upload_file('test/test.mp4', settings.AWS_STORAGE_BUCKET_NAME, 'video/천호어린이집,' + str(video_index) + ',kick' + '.mp4')
    elif hit_flag == 1 and kick_flag == 1:
        s3.upload_file('test/test.mp4', settings.AWS_STORAGE_BUCKET_NAME, 'video/천호어린이집,' + str(video_index) + ',hit,kick' + '.mp4')

    # test 폴더 삭제
    shutil.rmtree('test')

def upload_video():
    obj_list = s3.list_objects(Bucket=settings.AWS_STORAGE_BUCKET_NAME)
    contents_list = obj_list['Contents']

    if len(contents_list) != 0:
        key_list = [] # 검출된 프레임 담을 배열
        index, video_index = 0, 0
        hit_flag, kick_flag, cnt_no_kick_hit = 0, 0, 0
        tmp = 1
        while True:
            index += 1
            if is_not_valid_url(index):
                index -= 1
                continue
            flag = yolo.main(index)
            if flag != 0: # hit이나 kick이 검출되었으면
                if flag == 1:
                    hit_flag = 1
                else:
                    kick_flag = 1
                key_list.append(index)
            elif cnt_no_kick_hit == 10: # 마지막 검출된 후로부터 10프레임동안 검출되지 않았으면
                video_index += 1
                make_video(key_list, video_index, hit_flag, kick_flag)
                for i in range(tmp, key_list[-1]-10):
                    s3.delete_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=str(i)+'.jpg')
                tmp = key_list[-1]-10
                hit_flag, kick_flag, cnt_no_kick_hit = 0, 0, 0
                key_list = []
            elif len(key_list) != 0: # 검출되지 않았는데 key_list가 비어있지 않으면
                cnt_no_kick_hit += 1