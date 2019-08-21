'''
<pi camera 실습>
파이카메라를 활용하여 인공지능 훈련데이터 수집 준비하기
학습목표
-	파이카메라 특징 이해하기
-	카메라 세팅 방법 이해하기
-	연속적인 화면 재생과 화면 캡쳐 방법 배우기
'''

import time
import cv2

# 내장카메라 or 외장카메라에서 영상을 받아온다
# 0 = 카메라의 장치번호. 노트북에서 내장카메라는 장치번호가 0이다
# 카메라를 추가연결하여 외장카메라를 사용하는 경우, 장치번호가 1~n까지 변화한다
c = cv2.VideoCapture(0) 
time.sleep(0.1)
 
while(True):
    # cature.read(): 카메라의 상태 및 프레임을 받아옴
    # frame에 현재 프레임이 저장된다
    _,image = c.read()

    # 윈도우 창에 이미지를 띄운다
    cv2.imshow("Frame", image)

    # 키보드 입력이 있을 때까지 while 문을 반복한다
    # waitKey = 키보드 입력을 대기하는 함수. 0이면 입력이 있을 때까지 대기한다
    key = cv2.waitKey(1)

    # 키보드에서 q를 누르면 -> break
    if key == ord("q"):
        break

cv2.destroyAllWindows()