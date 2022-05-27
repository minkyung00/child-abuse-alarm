import cv2
import numpy as np
import time
from PIL import Image
import urllib.request
from io import BytesIO
import math
import matplotlib.pyplot as plt
from cvlib.object_detection import draw_bbox

import os
from django.conf import settings

#안 되는 경우 물체 하나만 정해서 직접 학습
#YOLO 네트워크 불러오기

def url_to_image(url):
  resp = urllib.request.urlopen(url)
  image = np.asarray(bytearray(resp.read()), dtype='uint8')
  image = cv2.imdecode(image, cv2.IMREAD_COLOR)
  return image

# 웹캠 신호 받기
CUR_DIR = os.path.dirname(__file__)
video_path = os.path.join(CUR_DIR, 'child_test_data.mp4')
VideoSignal = cv2.VideoCapture(video_path)
# VideoSignal = cv2.VideoCapture('child_test_data.mp4')
#weights, cfg 파일 불러와서 yolo 네트워크와 연결
# net = cv2.dnn.readNet("weight/yolov4-tiny_best-width.weights", "cfg/yolov4-tiny_width.cfg")
weights_path = os.path.join(CUR_DIR, './weight/yolov4-tiny_best-width.weights')
config_path =  os.path.join(CUR_DIR, './cfg/yolov4-tiny_width.cfg')
net = cv2.dnn.readNet(weights_path, config_path)

def crop_yolo(img, x,y,w,h,child_w,child_h):
    # frame.shape = 불러온 이미지에서 height, width, color 받아옴
    blank_w = 2*(child_w)
    blank_h=2*(child_h)
    ymin = y - blank_h
    ymax = y + h + blank_h
    xmin = x - blank_w
    xmax = x + w + blank_w
    if ymin < 0:
        ymin = 0
    if ymax > height:
        ymax = height
    if xmin < 0:
        xmin = 0
    if xmax > width:
        xmax = width
    crop = img[ymin:ymax, xmin:xmax]
    return crop



w = round(VideoSignal.get(3))
h = round(VideoSignal.get(4))
fps = VideoSignal.get(cv2.CAP_PROP_FPS)

# fourcc 값 받아오기, *는 문자를 풀어쓰는 방식, *'DIVX' == 'D', 'I', 'V', 'X'
fourcc = cv2.VideoWriter_fourcc(*'DIVX') #이건 동영상 저장해두려고 해놓은건데 저장이 잘 안 돼서 일단 보류,,,
# 1프레임과 다음 프레임 사이의 간격 설정
try:
    delay = round(1000 / fps)
except:
    ZeroDivisionError
# 웹캠으로 찰영한 영상을 저장하기
# cv2.VideoWriter 객체 생성, 기존에 받아온 속성값 입력
# YOLO NETWORK 재구성
classes = []
class_dir = os.path.join(CUR_DIR, 'capstone.names')
with open(class_dir, "r") as f:
    classes = [line.strip() for line in f.readlines()]
print(classes)
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
flag=0
list_ball_location=[]

frame = url_to_image(settings.AWS_S3_CUSTOM_DOMAIN + '/1.jpg')



height, width, c = frame.shape

# YOLO 입력
blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0),
True, crop=False)
net.setInput(blob)
outs = net.forward(output_layers)

class_ids = []
confidences = []
boxes = []
for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]

        # 검출 신뢰도
        if confidence > 0.5:
            # Object detected
            # 검출기의 경계상자 좌표는 0 ~ 1로 정규화되어있으므로 다시 전처리
            center_x = int(detection[0] * w)
            center_y = int(detection[1] * h)
            dw = int(detection[2] * w)
            dh = int(detection[3] * h)
            # Rectangle coordinate
            x = int(center_x - dw / 2)
            y = int(center_y - dh / 2)
            boxes.append([x, y, dw, dh])
            confidences.append(float(confidence))
            class_ids.append(class_id)

indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.45, 0.4)
child_w = 53
child_h = 118
for i in range(len(boxes)):
    if i in indexes:
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        if(label=='child'):
            child_w=w
            child_h=h
            #print(child_w,child_h)
        if(label=='hit'):
            if flag == 0:
                start = time.time()
                frame_cropped=crop_yolo(frame,x,y,w,h,child_w,child_h)
        score = confidences[i]

        # 경계상자와 클래스 정보 투영
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 5)
        cv2.putText(frame, label, (x, y - 20), cv2.FONT_ITALIC, 0.5, (255, 255, 255), 1)


cv2.imshow("YOLOv3", frame)
cv2.imshow("YOLOv3-crop",frame_cropped)
cv2.waitKey(0)