# <시범 운전하기>

# s: 운전모드/정지모드 토글방식
# -- 토글방식이란? 하나의 설정 값으로부터 다른 값으로 전환하는 것

# 방향키로 직진/좌회전/우회전/후진/부스터
# q;  프로그램 종료


# <훈련데이터 수집  및 정제>

# r: 데이터수집모드/데이터수정지모드 토글방식
# 방향키로 직진/좌회전/우회전/후진/부스터
# q;  프로그램 종료


# 모터 구동 모듈
import xhat as hw
import time
import cv2
import config as cfg

import os
import sys
import signal
import csv


# def: 파이썬에서 함수를 만들 때 사용하는 예약어
# data.csv 파일에 데이터 기록을 준비하는 메소드
def recording():

    # 현재 기록중인지 확인한다

    # 현재 기록중이면
    if cfg.recording:

        # 기록을 중지한다
        cfg.recording = False

        # 열려 있는 파일 객체를 닫는다
        cfg.f.close()

    #     현재 기록중이 아니면
    else:

        # 기록중 여부를 true로 바꾼다
        cfg.recording = True

        # 디렉토리가 설정되어 있지 않으면(기본값: training 폴더)
        if cfg.currentDir == '':

            # 디렉토리를 새로 만든다. 이름: 오늘 날짜
            cfg.currentDir = time.strftime('%Y-%m-%d')
            os.mkdir(cfg.outputDir+cfg.currentDir)

            # 새로만든 디렉토리에 있는 data.csv 파일을 '쓰기 모드'로 연다
            cfg.f=open(cfg.outputDir+cfg.currentDir+'/data.csv','w')

        #     디렉토리가 설정되어 있으면(기본값: training)
        else:

            # 원래 있던 data.csv 파일을 '추가모드'로 연다
            cfg.f=open(cfg.outputDir+cfg.currentDir+'/data.csv','a')

        #     위에서 오픈한 파일 객체를 writer 객체에 담는다
        cfg.fwriter = csv.writer(cfg.f)



def saveimage():

    # 현재 기록중이라면
    if cfg.recording:

        # 이미지 파일의 이름을 지정한다(img_현재시각_카운트.jpg)
        myfile = 'img_'+time.strftime('%Y-%m-%d_%H-%M-%S')+'_'+str(cfg.cnt)+'.jpg'

        # 콘솔에 파일 이름과 방향키 값을 출력한다
        # 방향키 값 예시) 0:stop, 1:left, 2:strait, 3:right, 4: back, 5: booster
        print(myfile, cfg.wheel)

        # 현재 열려있는 .cvs 파일에 한 라인을 추가한다
        # 내용: 새로 찍은 사진파일의 이름, 방향키 값(','로 구분한다)
        cfg.fwriter.writerow((myfile, cfg.wheel))

        # imwrite : 변환된 이미지나 동영상의 특정 프레임을 저장하는 함수
        # (저장할 파일 이름, 저장할 이미지)
        cv2.imwrite(cfg.outputDir+cfg.currentDir+'/'+ myfile, full_image)

        cfg.cnt += 1

        


# 이게 뭐지???????????
if __name__ == '__main__':

    # 아직 운전 실행 전 상태
    start_flag = False

    # 카메라를 켠다(내장카메라 or 외장카메라에서 영상을 받아온다)
    c = cv2.VideoCapture(0)
    c.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    c.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

    # 프레임 속도 -- 이거 왜 주석처리? 커스텀을 위해서?
    #c.set(cv2.CAP_PROP_FPS, 15)


    # 계속해서 아래 동작을 반복한다
    # 1. 사진을 찍어서 저장한다
    # 2. 사용자의 키보드 입력값을 받아서 -> 운전 시작/중지, 기록 시작/중지, 운전 방향을 판단한다
    while(True):

        # 언더스코어 왜 쓰는거지?
        # cature.read(): 카메라의 상태 및 프레임을 받아옴
        # frame에 현재 프레임이 저장된다
        _,full_image = c.read()

        # 윈도우 창에 이미지를 띄운다
        cv2.imshow('frame',full_image)


        # 사용자의 입력을 기다린다
        k = cv2.waitKey(5)

        # 사용자의 입력값에 따라 다른 코드를 실행한다

        # q: 중지
        if k == ord('q'):  #'q' key to stop program
            break

        # s: 시작/중지 토글
        """ Toggle Start/Stop motor movement """
        if k == 115: #115:'s'

            # 멈춰있는 상태였다면
            if start_flag == False:

                # 실행상태로 바꾼다
                start_flag = True

            #     실행상태였다면
            else:
                # 멈춤상태로 바꾼다
                start_flag = False

            #     flag 값을 콘솔에 출력한다
            print('start flag:',start_flag)


        # r: 기록 on/off
        """ Toggle Record On/Off  """
        if k == 114: #114:'r'

            # 레코드 함수를 실행한다
            recording()

            # 현재 레코딩 상태라면
            if cfg.recording:

               #  실행상태로 바꾼다
               # r 키를 누르면 자동으로 실행상태로 전환된다는 의미
               start_flag = True

            #    현재 레코딩 상태가 아니라면
            else:
               start_flag = False

               # 카운트 초기화
               cfg.cnt = 0
            print('cfg.recording:',cfg.recording)

        #save image files and images list file
        # 현재 기록 상태라면
        if cfg.recording:

            # 찍은 사진을 저장한다
            saveimage()
            print(cfg.cnt)


        # 실행 상태라면
        if start_flag:

            # 사용자의 입력 값에 따라 차를 움직인다
            # Left arrow: 81, Right arrow: 83, Up arrow: 82, Down arrow: 84
            if k == 81: 
                hw.motor_one_speed(cfg.maxturn_speed)
                hw.motor_two_speed(cfg.minturn_speed)

                # cfg.wheel - data.cvs에 데이터를 쌓을 때, 좌회전/우회전/직진 등을 이 숫자로 표기한다
                cfg.wheel = 1
            if k == 83: 
                hw.motor_one_speed(cfg.minturn_speed)
                hw.motor_two_speed(cfg.maxturn_speed)
                cfg.wheel = 3
            if k == 82: 
                hw.motor_one_speed(cfg.normal_speed_right)
                hw.motor_two_speed(cfg.normal_speed_left)
                cfg.wheel = 2

        #         + 후진, 부스터 메소드 추가함
        
        else:
            hw.motor_one_speed(0)
            hw.motor_two_speed(0)
            cfg.wheel = 0


#         모터를 정지시키고, 모든 윈도우 창을 닫는다
hw.motor_clean()
cv2.destroyAllWindows()
