import cv2
import numpy as np
import time
import math
import matplotlib.pyplot as plt
# from cvlib.object_detection import draw_bbox
import urllib.request

import os
from django.conf import settings

#VALID HIT+ URL+ CROP
def url_to_image(url):
  resp = urllib.request.urlopen(url)
  image = np.asarray(bytearray(resp.read()), dtype='uint8')
  image = cv2.imdecode(image, cv2.IMREAD_COLOR)
  return image

def overlap(child_box,abuse_box):
    valid=1
    try:
        child_x,child_y,child_xw,child_yh=child_box
        abuse_x,abuse_y,abuse_xw,abuse_yh=abuse_box
        if(child_xw+child_x<abuse_x)|(child_yh+child_y<abuse_y)|(child_x>abuse_xw+abuse_x)|(child_y>abuse_yh+abuse_y):
            valid=0
    except:
        ValueError
    return valid

def crop_yolo(img, x,y,w,h,child_w,child_h,height,width):
    # frame.shape = 불러온 이미지에서 height, width, color 받아옴
    blank_w = 2*(child_w)
    blank_h= 2*(child_h)
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
    return crop,ymin,ymax,xmin,xmax
# 웹캠 신호 받기

def main(i):
    # cap = cv2.VideoCapture('capstone_data/child_test6.mp4')
    #weights, cfg 파일 불러와서 yolo 네트워크와 연결
    CUR_DIR = os.path.dirname(__file__)
    weights_path = os.path.join(CUR_DIR, './weight/yolov4-tiny_best-width.weights')
    config_path =  os.path.join(CUR_DIR, './cfg/yolov4-tiny_width.cfg')
    net = cv2.dnn.readNet(weights_path, config_path)
    

    t_sum=0
    t_cnt=0

    # YOLO NETWORK 재구성
    classes = []
    class_dir = os.path.join(CUR_DIR, 'capstone.names')
    with open(class_dir, "r") as f:
        classes = [line.strip() for line in f.readlines()]
    #print(classes)
    layer_names = net.getLayerNames()
    output_layers = [layer_names[int(i) - 1] for i in net.getUnconnectedOutLayers()]
    #print(net.getUnconnectedOutLayers())
    #print(output_layers)
    #print(layer_names)

    idx=0
    while True:
        # 웹캠 프레임
        #ret, frame = VideoSignal.read()
        idx+=1
        child_w = 0
        child_h = 0

        hit_w = 0
        hit_h = 0
        hit_x = 0
        hit_y = 0
        hit_flag = 0

        kick_x = 0
        kick_y = 0
        kick_h = 0
        kick_w = 0
        kick_flag = 0
        # ret, frame = cap.read()
        frame = url_to_image(settings.AWS_S3_CUSTOM_DOMAIN + '/' + str(i) + '.jpg')
        #frame = url_to_image('https://capstone1234.s3.ap-northeast-2.amazonaws.com/' + str(idx) + '.jpg')
        start = time.time()
        height, width, c = frame.shape
        child = []
        hit = []
        kick=[]
        child_flag = 0
        hit_flag = 0
        kick_flag=0
        valid = 1


        # YOLO 입력
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (608, 608), (0, 0, 0),
        True, crop=False)

        net.setInput(blob)
        outs = net.forward(output_layers)
        #print(len(outs))
        #print(outs)

        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]

                # 검출 신뢰도
                if confidence > 0.4:
                    # Object detected
                    # 검출기의 경계상자 좌표는 0 ~ 1로 정규화되어있으므로 다시 전처리
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    dw = int(detection[2] * width)
                    dh = int(detection[3] * height)
                    # Rectangle coordinate
                    x = int(center_x - dw / 2)
                    y = int(center_y - dh / 2)
                    boxes.append([x, y, dw, dh])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.3, 0.4)
        #indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.1, 0.1)
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                if label == ('child'):
                    child = [x, y, w, h]
                    score_child = confidences[i]
                    child_flag = 1
                    child_w = w
                    child_h = h
                    #print('child')
                    #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 5)
                if label == ('hit'):
                    hit = [x, y, w, h]
                    score_hit = confidences[i]
                    hit_flag = 1
                    hit_w = w
                    hit_h = h
                    hit_x = x
                    hit_y = y
                    #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 5)
                    #print('hit: %.3f' %(score_hit))

                if label == ('kick'):
                    kick = [x, y, w, h]
                    score_kick = confidences[i]
                    kick_flag = 1
                    kick_w = w
                    kick_h = h
                    kick_x = x
                    kick_y = y
                    #print('kick: %3f' %(score_kick))
                end = time.time()
                t = end - start            # 경계상자와 클래스 정보 투영
                #cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 5)
                cv2.putText(frame, label, (x, y - 20), cv2.FONT_ITALIC, 0.5, (255, 255, 255), 1)
        frame_cropped=frame.copy()
        if (hit_flag == 1 & child_flag == 1):
            valid = overlap(child, hit)
            try:
                cv2.rectangle(frame, (child[0], child[1]), (child[0] + child[2], child[1] + child[3]), (0, 255, 255), 5)  # 노란색
                cv2.rectangle(frame, (hit[0], hit[1]), (hit[0] + hit[2], hit[1] + hit[3]), (0, 255, 0), 5)  # 초록색
                frame_cropped,ymin,ymax,xmin,xmax = crop_yolo(frame, hit_x, hit_y, hit_w, hit_h, child_w, child_h, height, width)
                return valid, [xmin, ymin, xmax, ymax]
            except:
                ValueError
        elif (kick_flag == 1 & child_flag == 1):
            valid = overlap(child, kick)
            try:
                cv2.rectangle(frame, (child[0], child[1]), (child[0] + child[2], child[1] + child[3]), (0, 255, 255), 5)  # 노란색
                cv2.rectangle(frame, (kick[0], kick[1]), (kick[0] + kick[2], kick[1] + kick[3]), (0, 0, 255), 5)#빨간색
                frame_cropped,ymin,ymax,xmin,xmax = crop_yolo(frame, kick_x, kick_y, kick_w, kick_h, child_w, child_h, height, width)
                return valid, [xmin, ymin, xmax, ymax]
            except:
                ValueError
        else:
            valid = 0
            return valid, []
        #print(valid)
        # try:
        #     t_sum+=t
        #     t_cnt+=1
        #     #print(t_cnt)
        #     if t_cnt%100==0:
        #         print(t_sum / t_cnt)
        #     #print(f"{t:.5f} sec")
        # except:
        #     NameError
        # cv2.imshow("YOLOv3", frame_cropped)
        # #out.write(frame)
        # # 1ms 마다 영상 갱신
        # if cv2.waitKey(1) > 0:
        #     break
    #out.release
