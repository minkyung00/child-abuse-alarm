import cv2
import time
import numpy as np
import math
import copy
import matplotlib.pyplot as plt
# from cvlib.object_detection import draw_bbox
import urllib.request

import os

def dist(ax,ay,bx,by):
    d=math.sqrt(pow(bx-ax,2)+pow(by-ay,2))
    return d
def url_to_image(url):
  resp = urllib.request.urlopen(url)
  image = np.asarray(bytearray(resp.read()), dtype='uint8')
  image = cv2.imdecode(image, cv2.IMREAD_COLOR)
  return image

#pretrained 모델과 config file 이용해 네트워크 불러옴
# MPII에서 각 파트 번호, 선으로 연결될 POSE_PAIRS
Npart=16
#BODY_PARTS = {"Head": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
#              "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
#              "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "Chest": 14,
#              "Background": 15}

BODY_PARTS = ["Head", "Neck", "RShoulder", "RElbow", "RWrist",
              "LShoulder", "LElbow", "LWrist", "RHip", "RKnee",
              "RAnkle", "LHip", "LKnee", "LAnkle", "Chest",
              "Background"]
POSE_PAIRS = [[0,14],[0,1], [1,2], [2,3], [3,4], [1,5], [5,6], [6,7], [1,14], [14,8], [8,9], [9,10], [14,11], [11,12], [12,13]]

mapIdx = [[14,15],[16,17], [18,19], [20,21], [22,23], [24,25], [26,27], [28,29], [30,31], [32,33], [34,35], [36,37], [38,39], [40,41], [42,43]]
colors = [[0,100,255], [0,100,255], [0,255,255], [0,100,255], [0,255,255], [0,100,255],
         [0,255,0], [255,200,100], [255,0,255], [0,255,0], [255,200,100], [255,0,255],
         [0,0,255], [255,0,0], [200,200,0], [255,0,0]]

# 각 파일 path
CUR_DIR = os.path.dirname(__file__)
protoFile = os.path.join(CUR_DIR, "pose_deploy_linevec_faster_4_stages.prototxt")
weightsFile = os.path.join(CUR_DIR, "pose_iter_160000.caffemodel") #pretrained_model
device = 'cpu'

#PCM(part confidence maps) PAF(part affinity fields) 이용해 keypoint 찾아주기 - keypoint 이어주어 시각화

def getKeypoints(probMap, threshold=0.1):

    #probmap: output의 PCM 결과
    mapSmooth = cv2.GaussianBlur(probMap, (3, 3), 0, 0) #노이즈 제거
    mapMask = np.uint8(mapSmooth > threshold) #threshold 보다 큰 부분만
    #cv2.imshow('probmap',probMap)
    keypoints = []
    contours, _ = cv2.findContours(mapMask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)#외곽선 추출

    # NMS(non-maximum suppression: 얼마나 겹쳐있는지 판단) 사용해 keypoint 추출
    for cnt in contours:
        blobMask = np.zeros(mapMask.shape)#mapMask 크기의 빈 마스크 생성
        blobMask = cv2.fillConvexPoly(blobMask, cnt, 1) # points에 저장된 좌표로 이루어진 볼록다각형 or 일반 다각형을 color로 채운다
        maskedProbMap = mapSmooth * blobMask # 두 개를 곱한다.

        # maxVal = 있을 확률
        # maxLoc = x,y좌표
        _, maxVal, _, maxLoc = cv2.minMaxLoc(maskedProbMap)

        keypoints.append(maxLoc + (probMap[maxLoc[1], maxLoc[0]],)) #좌표 + probmap 지수
    return keypoints

# 서로 맺어질 수 있는 쌍 찾기
def findPairs(output,imgWidth,imgHeight,points): #output: network -imageld, PAF & PCM의 index(양 방향 학습해서 총 15개, height, width
    pairs_valid = []
    pairs_invalid = []

    n_interp_samples = 10
    paf_score_th = 0.1
    conf_th = 0.7

    for k in range(len(mapIdx)): #POSE_PAIRS 개수와 같음

        pafA = output[0, mapIdx[k][0], :, :] # k번째 part의 A-> B 방향
        pafB = output[0, mapIdx[k][1], :, :] # k번째 part의 B-> A 방향

        pafA = cv2.resize(pafA, (imgWidth, imgHeight)) #image에 맞게 resize
        pafB = cv2.resize(pafB, (imgWidth, imgHeight))


        candA = points[POSE_PAIRS[k][0]] #candA : k번째 part의 A keypoint들
        candB = points[POSE_PAIRS[k][1]] #candB : k번째 part의 B keypoint들

        #첫번째 part----------------------------
        #candA: [(314, 42, 0.6863895, 0), (279, 37, 0.62600565, 1), (143, 31, 0.7250983, 2), (110, 31, 0.6882536, 3), (76, 30, 0.7219929, 4), (183, 25, 0.79937786, 5)]
        #candB: [(309, 72, 0.6747359, 6), (274, 65, 0.6824692, 7), (144, 59, 0.9170951, 8), (99, 58, 0.6678957, 9), (65, 55, 0.7179112, 10), (184, 54, 0.85833365, 11)]

        #두번째 part----------------------------
        #candA: [(309, 72, 0.6747359, 6), (274, 65, 0.6824692, 7), (144, 59, 0.9170951, 8), (99, 58, 0.6678957, 9), (65, 55, 0.7179112, 10), (184, 54, 0.85833365, 11)]
        #candB:  [(292, 77, 0.5027799, 12), (256, 71, 0.4919345, 13), (126, 69, 0.6564072, 14), (83, 65, 0.42105174, 15), (172, 60, 0.61953044, 16), (49, 54, 0.72677803, 17)]

        nA = len(candA) #인원수 와 동일
        nB = len(candB)

        if (nA != 0 and nB != 0):
            valid = np.zeros((0, 3))
            for i in range(nA):#여러 개의 B중에서 올바른 B를 찾는 과정
                max_idx = -1
                maxScore = -1
                found = 0
                for j in range(nB):
                    # 단위 벡터 찾기
                    d_ij = np.subtract(candB[j][:2], candA[i][:2])
                    norm = np.linalg.norm(d_ij) #norm 구하기
                    if norm: #단위벡터 계산
                        d_ij = d_ij / norm
                    else:
                        continue
                    #p(u)- limb 위에 있을 거라고 예상되는 pixel들
                    inner_coord = list(zip(np.linspace(candA[i][0], candB[j][0], num=n_interp_samples),
                                            np.linspace(candA[i][1], candB[j][1], num=n_interp_samples))) #linspace로 구간 내 숫자 채우고 zip으로 데이터 엮기
                    # paf 저장
                    paf_inner = []
                    for k in range(len(inner_coord)):
                        paf_inner.append([pafA[int(round(inner_coord[k][1])), int(round(inner_coord[k][0]))],
                                           pafB[int(round(inner_coord[k][1])), int(round(inner_coord[k][0]))]])
                    # Find E : 최종 E 찾기
                    paf_scores = np.dot(paf_inner, d_ij)#paf score 계산
                    avg_paf_score = sum(paf_scores) / len(paf_scores) #평균 paf score 찾기

                    if (len(np.where(paf_scores > paf_score_th)[0]) / n_interp_samples) > conf_th:
                        if avg_paf_score > maxScore:#max score 찾기
                            max_idx = j
                            maxScore = avg_paf_score
                            found = 1

                if found:
                    valid = np.append(valid, [[candA[i][3], candB[max_idx][3], maxScore]], axis=0)

            pairs_valid.append(valid)

        else: #keypoints를 찾지 못했을 때
            #print("No Connection : k = {}".format(k))
            pairs_invalid.append(k)
            pairs_valid.append([])
    #print(pairs_valid) #좌표, overall score
    return pairs_valid,pairs_invalid

#머리,손,발 검출 안되면 삭제
def head_hand_foot(hit_or_kick,person_Keypoints):
    no_match_flag = 0
    for n in range(len(person_Keypoints)):
        n = n - no_match_flag
        if (person_Keypoints[n][0] == -1 ):
            person_Keypoints = np.delete(person_Keypoints, n, axis=0)
            no_match_flag += 1
        elif (person_Keypoints[n][14]==-1):
            person_Keypoints = np.delete(person_Keypoints, n, axis=0)
            no_match_flag += 1
        else:
            if (hit_or_kick == 1):
                if (person_Keypoints[n][4] == -1) & (person_Keypoints[n][7] == -1):
                    person_Keypoints = np.delete(person_Keypoints, n, axis=0)
                    no_match_flag += 1
            if (hit_or_kick == 2):
                if (person_Keypoints[n][10] == -1) & (person_Keypoints[n][13] == -1):
                    person_Keypoints = np.delete(person_Keypoints, n, axis=0)
                    no_match_flag += 1
    return person_Keypoints

def head_moving(person_Keypoints,backbone,head,keypoints_list): # 전 frame의 backbone, head 좌표
    no_match_flag = 0
    for n in range(len(person_Keypoints)):
        n=n-no_match_flag
        index = person_Keypoints[n][np.array(POSE_PAIRS[0])]
        print("%d in range %d" %(n,len(person_Keypoints)))
        if -1 in index:
            continue
        B = np.int32(keypoints_list[index.astype(int), 0])
        A = np.int32(keypoints_list[index.astype(int), 1])
        head_dist=dist(head[n][0],head[n][1],A[0],A[1])#이전 프레임과 현재 프레임의 head_dist 계산
        if ((head_dist/backbone[n])>=0.3):
            person_Keypoints = np.delete(person_Keypoints, n, axis=0)
            backbone=np.delete(backbone,n,axis=0)
            no_match_flag += 1
            print('no match')
        print(head_dist/backbone[n])
    return person_Keypoints
# 각 사람의 keypoints list 생성
def getPerson_Keypoints(pairs_valid,pairs_invalid,keypoints_list):
    person_Keypoints = -1 * np.ones((0, 16)) # [] 생성
    for k in range(len(POSE_PAIRS)):
       # print("<%d>"%k)
        if k not in pairs_invalid:
            partAs = pairs_valid[k][:, 0]
            partBs = pairs_valid[k][:, 1]
            indexA, indexB = np.array(POSE_PAIRS[k]) #POSE_PAIRS 읽어오기

            for i in range(len(pairs_valid[k])): #인원 수만큼
                found = 0
                person_idx = -1
                for j in range(len(person_Keypoints)): #인원 수만큼
                    if person_Keypoints[j][indexA] == partAs[i]:
                        person_idx = j
                        found = 1
                        break
                if found:
                    person_Keypoints[person_idx][indexB] = partBs[i]
                    person_Keypoints[person_idx][-1] += keypoints_list[partBs[i].astype(int), 2] + pairs_valid[k][i][2]

                # partA가 없을 시 하나 새로 생성
                elif not found and k < 14:
                    row = -1 * np.ones(16)
                    row[indexA] = partAs[i]
                    row[indexB] = partBs[i]
                    row[-1] = sum(keypoints_list[pairs_valid[k][i, :2].astype(int), 2]) + pairs_valid[k][i][2]
                    person_Keypoints = np.vstack([person_Keypoints, row])
    return person_Keypoints

def main(hit_or_kick, frame):
    net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)#네트워크 읽어오기

    if device == "cpu":
        net.setPreferableBackend(cv2.dnn.DNN_TARGET_CPU)
        print("Using CPU device")
    elif device == "gpu":
        net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
        net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
        print("Using GPU device")

    # cap = cv2.VideoCapture('capstone_data/child_test6.mp4') #영상 불러오기

    #w = round(cap.get(3))
    #h = round(cap.get(4))
    #fps = cap.get(cv2.CAP_PROP_FPS)


    frame_cnt=0
    # hit_or_kick=1#받아와야 함
    person_bf=0
    dist_abuse=0 #이동거리 d / 척추 길이 backbone
    abuse_flag=0
    # idx=1
    abuse_thres=0.08  #dist_abuse 기준

    for img_idx in range(len(frame)):
        img = frame[img_idx]
        # 웹캠 프레임
        # ret, img = cap.read()
        start=time.time()
        # img = url_to_image('https://capstone1234.s3.ap-northeast-2.amazonaws.com/' + str(idx) + '.jpg')
        frame_cnt+=1

        if frame_cnt==1:#초기값 설정
            joints = 4
            xy = 2
            dist_point= [[[0 for _ in range(xy)]for _ in range(joints)] for _ in range(30)]#임의값 30으로 설정
            head=[[0 for _ in range(xy)]for _ in range(30)]

        # idx+=1
        if (frame_cnt==1)|(frame_cnt % 5 == 0):
            print("------------------------------")
            print("frame_cnt :", frame_cnt)
            # frame.shape = 불러온 이미지에서 height, width, color 받아옴
            imgHeight, imgWidth, _ = img.shape
            inputHeight = 368
            inputWidth = int((inputHeight / imgHeight) * imgWidth)

            inpBlob = cv2.dnn.blobFromImage(img,
                                            1.0 / 255, (inputWidth, inputHeight),
                                            (0, 0, 0), swapRB=False, crop=False)

            net.setInput(inpBlob)
            output = net.forward() #imageld, PAF & PCM의 index(양 방향 학습해서 총 15개, height, width


            points = []
            keypoints_list = np.zeros((0, 3))
            keypoint_id = 0
            threshold = 0.1

            for part in range(Npart): #각 부위별로
                probMap = output[0, part, :, :]
                probMap = cv2.resize(probMap, (imgWidth, imgHeight))
                keypoints = getKeypoints(probMap, threshold) #여덟 명이면 여덟 개 출력

                #각 인물에 대한 part 좌표 추출: 차례대로 "Head -> Neck -> RShoulder -> RElbow -> RWrist" ~~
                # [(314, 42, 0.6863895), (279, 37, 0.62600565), (143, 31, 0.7250983), (110, 31, 0.6882536), (76, 30, 0.7219929), (183, 25, 0.79937786)]
                try:
                    x=keypoints[0][0] #part의  x좌표
                    y=keypoints[0][1] #part의  y좌표
                except: IndexError


                keypoints_with_id = []
                for i in range(len(keypoints)):
                    keypoints_with_id.append(keypoints[i] + (keypoint_id,)) #keypoints에 id 포함해 저장
                    keypoints_list = np.vstack([keypoints_list, keypoints[i]])#수직적 행렬 결합 -> keypoints를 수직으로 저장
                    keypoint_id += 1
                #keypoints_with_id : 각 인물에 id 부여
                #[(314, 42, 0.6863895, 0), (279, 37, 0.62600565, 1), (143, 31, 0.7250983, 2), (110, 31, 0.6882536, 3), (76, 30, 0.7219929, 4), (183, 25, 0.79937786, 5)]

                #keypoints_list: 수직으로 결합
                # [[314.          42.           0.68638951]
                #  [279.          37.           0.62600565]
                #  [143.          31.           0.72509831]
                #  [110.          31.           0.68825358]
                #  [ 76.          30.           0.72199291]
                #  [183.          25.           0.79937786]]
                points.append(keypoints_with_id)

            #imageCopy = image.copy()
           # for i in range(Npart):# 각 부위별로
                #for j in range(len(points[i])):# 인원수만큼
                    #cv2.circle(imageCopy, points[i][j][0:2], 5, [0, 0, 255], -1, cv2.LINE_AA) #points: red


            pairs_valid, pairs_invalid = findPairs(output,imgWidth,imgHeight,points)
            person_Keypoints = getPerson_Keypoints(pairs_valid, pairs_invalid,keypoints_list)

            person=[]

            person_Keypoints = head_hand_foot(hit_or_kick,person_Keypoints)
            person = len(person_Keypoints)
            backbone = []
            for i in range(Npart - 1):
                for n in range(person):
                    index = person_Keypoints[n][np.array(POSE_PAIRS[i])]
                    if -1 in index:
                        continue
                    B = np.int32(keypoints_list[index.astype(int), 0])
                    A = np.int32(keypoints_list[index.astype(int), 1])
                   # cv2.line(imageCopy, (B[0], A[0]), (B[1], A[1]), colors[i], 3, cv2.LINE_AA)
                    if i == 0:
                        backbone.append(dist(B[0], A[0], B[1], A[1])) # backbone 계산
                        #head[n][0]=A[0]
                        #head[n][1]=A[1]
                        #print(backbone)
                    elif (i==4):
                        d = dist(dist_point[n][0][0], dist_point[n][0][1], A[0], A[1])
                        dist_point[n][0][0]=A[0]
                        dist_point[n][0][1]=A[1] #관절 좌표 저장
                        dist_abuse=d/(backbone[n]*5)
                        print("left_hand ", dist_abuse)
                        if (dist_abuse> abuse_thres) & (frame_cnt > 1):
                            abuse_flag = 1
                    elif (i==7):
                        d = dist(dist_point[n][0][0], dist_point[n][0][1], A[0], A[1])
                        dist_point[n][0][0]=A[0]
                        dist_point[n][0][1]=A[1] #관절 좌표 저장
                        dist_abuse = d / (backbone[n] * 5)
                        print("right_hand ", dist_abuse)
                        if (dist_abuse> abuse_thres) & (frame_cnt > 1):
                            abuse_flag = 1
                    elif (i==11):
                        d = dist(dist_point[n][0][0], dist_point[n][0][1], A[0], A[1])
                        dist_point[n][0][0]=A[0]
                        dist_point[n][0][1]=A[1] #관절 좌표 저장
                        dist_abuse=d/(backbone[n]*5)
                        print("left_foot ", dist_abuse)
                        if (dist_abuse> abuse_thres) & (frame_cnt > 1):
                            abuse_flag = 1
                    elif (i==14):
                        d = dist(dist_point[n][0][0], dist_point[n][0][1], A[0], A[1])
                        dist_point[n][0][0]=A[0]
                        dist_point[n][0][1]=A[1] #관절 좌표 저장
                        dist_abuse=d/(backbone[n])
                        print("right_foot ", dist_abuse)
                        if (dist_abuse> abuse_thres) & (frame_cnt > 1):
                            abuse_flag = 1
            print("abuse_flag: ", abuse_flag)
        #print("time",end-start)
            # cv2.imshow('openpose',img)
        if cv2.waitKey(1) == 27:
            break
    return abuse_flag
# main()