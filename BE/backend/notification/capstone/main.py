import boto3
import os
import shutil
import urllib.request
from urllib.error import HTTPError
import cv2
import numpy as np

from . import yolo_child_abuse
from . import openpose_multi_person_3

from django.conf import settings
from notification.views import save_notification

# accessKey = 'AKIA2UJDATHMOCFHIMPA'
# secretKey = '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'
# region = 'ap-northeast-2'
# bucket_name = 'capstone1234'

s3 = boto3.client(
    's3',
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    region_name=settings.AWS_REGION
    )
# for i in range(1, 100):
#     s3.upload_file('tmp_data/'+str(i)+'.jpg', bucket_name, str(i)+'.jpg')

# # 없는 url이면 True 반환
def is_not_valid_url(index):
    url = settings.AWS_S3_CUSTOM_DOMAIN + '/' + str(index) + '.jpg'
    try:
        resp = urllib.request.urlopen(url)
    except HTTPError as e:
        return True
    return False

def url_to_image(url):
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype='uint8')
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

def crop_image(img, crop_xy):
    img = img[crop_xy[1]:crop_xy[3], crop_xy[0]:crop_xy[2]]
    return img

def make_video(key_list, video_index, hit_flag, kick_flag, hit_cnt, kick_cnt):
    print('hit_cnt:', hit_cnt, "kick_cnt:", kick_cnt)
    for i in range(key_list[0]-10, key_list[-1]+10):
        if i <= 0 or i in key_list:
            continue
        key_list.append(i)
    key_list.sort()
    print('key_list:', key_list)
    # test 폴더 없으면 만들기
    if not os.path.isdir('test'):
        os.mkdir('test')

    # s3에서 img 받아오기
    for i in range(len(key_list)):
        if is_not_valid_url(key_list[i]):
            continue
        print("key_list[i]: ", str(key_list[i]))
        s3.download_file(settings.AWS_STORAGE_BUCKET_NAME, str(key_list[i]) + '.jpg', 'test/' + str(key_list[i]) + '.jpg')

    # 동영상 만들기
    os.system(f'ffmpeg -r 2 -pattern_type glob -i "test/*.jpg"'
              f' -crf 20 test/test.mp4')

    # 동영상 s3에 업로드
    if hit_flag == 1 and kick_flag == 0:
        print('UPLOAD VIDEO')
        s3.upload_file('test/test.mp4', settings.AWS_STORAGE_BUCKET_NAME, 'video/천호어린이집,' + str(video_index) + ',hit,' + str(hit_cnt) + '.mp4')
        save_notification('천호어린이집', str(video_index) + ',hit,' + str(hit_cnt))
    elif hit_flag == 0 and kick_flag == 1:
        print('UPLOAD VIDEO')
        s3.upload_file('test/test.mp4', settings.AWS_STORAGE_BUCKET_NAME, 'video/천호어린이집,' + str(video_index) + ',kick,' + str(kick_cnt) + '.mp4')
        save_notification('천호어린이집', str(video_index) + ',kick,' + str(kick_cnt))
    elif hit_flag == 1 and kick_flag == 1:
        print('UPLOAD VIDEO')
        s3.upload_file('test/test.mp4', settings.AWS_STORAGE_BUCKET_NAME, 'video/천호어린이집,' + str(video_index) + ',hit,' + str(hit_cnt) + ',kick,' + str(kick_cnt) + '.mp4')
        save_notification('천호어린이집', str(video_index) + ',hit kick,' + str(hit_cnt)+ ',' + str(kick_cnt))

    # test 폴더 삭제
    shutil.rmtree('test')

def upload_video():
    obj_list = s3.list_objects(Bucket = settings.AWS_STORAGE_BUCKET_NAME)
    print(obj_list)
    contents_list = obj_list['Contents']
    if len(contents_list) != 0:
        key_list = [] # 검출된 프레임 담을 배열
        index, video_index = 0, 0
        hit_flag, kick_flag, cnt_no_kick_hit = 0, 0, 0
        hit_cnt, kick_cnt = 0, 0
        tmp = 1
        while True:
            index += 1
            print("index:", index)
            if is_not_valid_url(index):
                print("in")
                index -= 1
                continue
            flag, cropped = yolo_child_abuse.main(index)
            print("flag: ", flag)
            # print(cropped)
            # cropped : [xmin, ymin, xmax, ymax]
            if flag != 0: # hit이나 kick이 검출되었으면
                print('검출된 index:', index)
                frame_list = []
                for i in range(index-5, index+6):
                    if i <= 0:
                        continue
                    if is_not_valid_url(i):
                        i -= 1
                        continue
                    print('list:', i)
                    frame1 = url_to_image(settings.AWS_S3_CUSTOM_DOMAIN + '/' + str(i) + '.jpg')
                    cropped_image = crop_image(frame1, cropped)
                    frame_list.append(cropped_image)
                openpose_flag = openpose_multi_person_3.main(flag, frame_list)
                print('openpose_flag:', openpose_flag)
                # openpose_flag: 0 -> 검출안된 거, 1 -> 검출된 거
                # print('openpose_flag:', openpose_flag)
                # cv2.imshow('img', crop_image(frame1, cropped))
                # cv2.imwrite('img.jpg', crop_image(frame1, cropped))
                if openpose_flag == 1:
                    if flag == 1:
                        hit_flag = 1
                        hit_cnt += 1
                    else:
                        kick_flag = 1
                        kick_cnt += 1
                    key_list.append(index)
                    index += 5
            elif cnt_no_kick_hit == 10: # 마지막 검출된 후로부터 10프레임동안 검출되지 않았으면
                video_index += 1
                make_video(key_list, video_index, hit_flag, kick_flag, hit_cnt, kick_cnt)
                # for i in range(tmp, key_list[-1]-10):
                #     s3.delete_object(Bucket=bucket_name, Key=str(i)+'.jpg')
                tmp = key_list[-1]-10
                hit_flag, kick_flag, cnt_no_kick_hit = 0, 0, 0
                hit_cnt, kick_cnt = 0, 0
                key_list = []
            elif len(key_list) != 0: # 검출되지 않았는데 key_list가 비어있지 않으면
                cnt_no_kick_hit += 1