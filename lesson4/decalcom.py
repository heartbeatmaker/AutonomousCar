'''
훈련데이터 분석 과정 2

좌우이미지 반전 데이터 만들기

데이터를 수집하다 보면, 좌회전 데이터가 더 많거나 우회전 데이터가 더 많을 수도 있다
아래 코드를 통해, 수집한 데이터를 좌우 반전시킨 데이터를 더 만들어낸다
데이터 분포(좌회전, 우회전 데이터의 비율)을 균등하게 맞출 수 있고, 데이터의 양을 증가시킬 수 있다
'''


import scipy.misc
import cv2
import random
import csv
#from mlxtend.preprocessing import one_hot
import numpy as np
import config as cfg



# data.csv 파일에 원본 데이터만 남긴다(전에 만들어놓은 좌우반전 데이터를 삭제한다)
#delete dc_img* in data.csv file
originalrows = []
with open('data/' + cfg.currentDir + '/data.csv', newline='') as csvfile:
    filereader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in filereader:
        #print(row[0], row[1])

        # dc_라는 이름으로 시작하는 파일: 좌우 반전 용으로 새로 생성된 파일
        if row[0][:2] != 'dc':
            originalrows.append(row)

# 'w'모드로 파일을 쓰면, 해당 파일에 기존에 기록되어 있던 데이터는 사라진다
with open('data/' + cfg.currentDir + '/data.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|')
    filewriter.writerows(originalrows)


x1 = []
#y1 = []
x2 = []
x3 = []
#y3 = []


# 각각의 방향 값에 해당하는 이미지 경로를 리스트에 담는다
#read data.csv
with open('data/' + cfg.currentDir + '/data.csv', newline='') as csvfile:
    filereader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in filereader:
        #print(row[0], row[1])

        # 좌
        if int(row[1]) == 1:
            x1.append(row[0])

        # 직진
        elif int(row[1]) == 2:
            x2.append(row[0])

        # 우
        elif int(row[1]) == 3:
            x3.append(row[0])


# data.csv 파일에 데이터를 추가하기 시작
cfg.f=open(cfg.outputDir+cfg.currentDir+'/data.csv','a')
cfg.fwriter = csv.writer(cfg.f)


# 좌회전 데이터를 좌우대칭하여 저장한다
for i in range(len(x1)):
    full_image = cv2.imread('data/' + cfg.currentDir + '/' + x1[i] , cv2.IMREAD_COLOR)

    # flip: 이미지 대칭 함수. 상하 or 좌우 대칭이 가능하다
    # cv2.flip(원본 이미지, 대칭 방법)
    # 0: 상하대칭 / 1: 좌우대칭

    # 이미지를 좌우로 대칭한다
    full_image = cv2.flip(full_image, 1)

    # 이미지 이름 맨 앞에 dc_를 붙인다
    myfile = 'data/' + cfg.currentDir + '/dc_' + x1[i]

    # 이미지 저장
    cv2.imwrite(myfile,full_image)

    # data.csv 파일에 데이터를 추가한다
    # writerow()의 함수 parameter에 list[]값을 넣으면 column에 순서대로 write됨
    # 이미지 경로, 3(=우회전 방향값) 을 컬럼에 저장한다
    '''
    좌회전 데이터를 좌우반전 했으므로, 우회전 데이터로 저장해야 한다
    '''
    cfg.fwriter.writerow(('dc_' + x1[i], 3))


# 우회전 데이터를 좌우대칭하여 저장한다
for i in range(len(x3)):
    full_image = cv2.imread('data/' + cfg.currentDir + '/' + x3[i] , cv2.IMREAD_COLOR)
    full_image = cv2.flip(full_image, 1)
    myfile = 'data/' + cfg.currentDir + '/dc_' + x3[i]
    cv2.imwrite(myfile,full_image)
    '''
    우회전 데이터를 좌우반전 했으므로, 좌회전 데이터로 저장해야 한다
    '''
    cfg.fwriter.writerow(('dc_' + x3[i], 1))



# 직진 데이터를 좌우대칭하여 저장한다
for i in range(len(x2)):
    full_image = cv2.imread('data/' + cfg.currentDir + '/' + x2[i] , cv2.IMREAD_COLOR)
    full_image = cv2.flip(full_image, 1)
    myfile = 'data/' + cfg.currentDir + '/dc_' + x2[i]
    cv2.imwrite(myfile,full_image)
    '''
    직진 데이터를 좌우반전 했으므로, 원본과 동일하게 직진 데이터로 저장해야 한다
    '''
    cfg.fwriter.writerow(('dc_' + x2[i], 2))


