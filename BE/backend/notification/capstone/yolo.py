import cv2
import numpy as np
import time
import math
import matplotlib.pyplot as plt
# from cvlib.object_detection import draw_bbox
import urllib.request
import os

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def url_to_image(url):
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype='uint8')
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

#안 되는 경우 물체 하나만 정해서 직접 학습
#YOLO 네트워크 불러오기
def overlap(child_box,abuse_box):
    valid=1
    try:
        child_x,child_y,child_xw,child_yh=child_box
        abuse_x,abuse_y,abuse_xw,abuse_yh=abuse_box
        #print(child_x,child_y,child_xw+child_x,child_yh+child_y)
        #print(hit_x,hit_y,hit_xw+hit_x,hit_yh+hit_y)
        if(child_xw+child_x<abuse_x)|(child_yh+child_y<abuse_y)|(child_x>abuse_xw+abuse_x)|(child_y>abuse_yh+abuse_y):
            valid=0
    except:
        ValueError
    return valid

def main(i):
    CUR_DIR = os.path.dirname(__file__)
    # 웹캠 신호 받기
    video_path = os.path.join(CUR_DIR, 'child_test_data.mp4')
    VideoSignal = cv2.VideoCapture(video_path)
    #weights, cfg 파일 불러와서 yolo 네트워크와 연결
    weights_path = os.path.join(CUR_DIR, './weight/yolov4-tiny_best-width.weights')
    config_path =  os.path.join(CUR_DIR, './cfg/yolov4-tiny_width.cfg')
    net = cv2.dnn.readNet(weights_path, config_path)
    # net = cv2.dnn.readNet('weight/yolov4-tiny_best-width.weights', 'cfg/yolov4-tiny_width.cfg')
    #print(net)
    #print(type(net))
    #print(net.getLayerNames)
    #VideoSignal = cv2.VideoCapture('data/child_test_data.mp4')
    #weights, cfg 파일 불러와서 yolo 네트워크와 연결
    #net = cv2.dnn.readNet("weight/yolov4-tiny_best-width.weights", "cfg/yolov4-tiny_width.cfg")

    w = round(VideoSignal.get(3))
    h = round(VideoSignal.get(4))
    fps = VideoSignal.get(cv2.CAP_PROP_FPS)

    t_sum=0
    t_cnt=0
    # fourcc 값 받아오기, *는 문자를 풀어쓰는 방식, *'DIVX' == 'D', 'I', 'V', 'X'
    fourcc = cv2.VideoWriter_fourcc(*'DIVX') #이건 동영상 저장해두려고 해놓은건데 저장이 잘 안 돼서 일단 보류,,,
    # 1프레임과 다음 프레임 사이의 간격 설정
    try:
        delay = round(1000 / fps)
    except:
        ZeroDivisionError
    # 웹캠으로 찰영한 영상을 저장하기
    # cv2.VideoWriter 객체 생성, 기존에 받아온 속성값 입력
    out = cv2.VideoWriter('output_yolo.avi', fourcc, fps, (w, h)) #output.avi로 저장
    # YOLO NETWORK 재구성
    classes = []
    class_dir = os.path.join(CUR_DIR, 'capstone.names')
    with open(class_dir, "r") as f:
        classes = [line.strip() for line in f.readlines()]
    # print(classes)
    layer_names = net.getLayerNames()
    output_layers = [layer_names[int(i) - 1] for i in net.getUnconnectedOutLayers()]
    # print(net.getUnconnectedOutLayers())
    # print(output_layers)
    # print(layer_names)


    while True:
        # 웹캠 프레임
        # ret, frame = VideoSignal.read()
        start = time.time()
        frame = url_to_image('https://capstone1234.s3.ap-northeast-2.amazonaws.com/' + str(i) + '.jpg')
        h, w, c = frame.shape
        child = []
        hit = []
        kick=[]
        child_flag = 0
        hit_flag = 0
        kick_flag=0
        valid = 1


        # YOLO 입력
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0),
        True, crop=False)

        #print(blob)
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
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                if label == ('child'):
                    child = [x, y, w, h]
                    score_child = confidences[i]
                    child_flag = 1
                    # print('child')
                if label == ('hit'):
                    hit = [x, y, w, h]
                    score_hit = confidences[i]
                    hit_flag = 1
                    # print('hit')
                if label == ('kick'):
                    kick = [x, y, w, h]
                    score_kick = confidences[i]
                    kick_flag = 1
                    # print('kick')
                end = time.time()
                t = end - start
                # 경계상자와 클래스 정보 투영
                #cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 5)
                # cv2.putText(frame, label, (x, y - 20), cv2.FONT_ITALIC, 0.5, (255, 255, 255), 1)
        if (hit_flag == 1 & child_flag == 1):
            valid = overlap(child, hit)
            return valid # 1이면 hit검출 / 0이면 검출안된거고
            # try:
            #     cv2.rectangle(frame, (child[0], child[1]), (child[0] + child[2], child[1] + child[3]), (0, 255, 255), 5)  # 노란색
            #     cv2.rectangle(frame, (hit[0], hit[1]), (hit[0] + hit[2], hit[1] + hit[3]), (0, 255, 0), 5)  # 초록색
            # except:
            #     ValueError
        elif (kick_flag == 1 & child_flag == 1):
            valid = overlap(child, kick)
            return valid # 2이면 kick검출
            # try:
            #     cv2.rectangle(frame, (child[0], child[1]), (child[0] + child[2], child[1] + child[3]), (0, 255, 255), 5)  # 노란색
            #     cv2.rectangle(frame, (kick[0], kick[1]), (kick[0] + kick[2], kick[1] + kick[3]), (0, 0, 255), 5)#빨간색
            # except:
            #     ValueError
        else:
            valid = 0
            return valid
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
        cv2.imshow("YOLOv3", frame)
        #out.write(frame)
        # 1ms 마다 영상 갱신
        if cv2.waitKey(1) > 0:
            break


    #out.release

main(1)
