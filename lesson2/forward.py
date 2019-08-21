# 모터 구동 모듈
# hw라는 이름으로 xhat 모듈을 참조한다
import xhat as hw

# opencv 를 import 한다. cv2 = opencv 의 패키지 이름
import cv2

# 이미지를 화면에 띄운다
img = cv2.imread('images.png')
cv2.imshow('image',img)

# 시작 플래그를 false로 둔다
start_flag = False

while (True):

    # waitKey = 키보드 입력을 대기하는 함수. 0이면 입력이 있을 때까지 대기한다
    # 이 경우, 5ms 동안 키보드 입력을 기다린다
    # waitKey 의 리턴값: int(ASCII 숫자)
    k = cv2.waitKey(5)

    # 이게 뭐지?
    # waitKey의 값?
    if k != -1:
        print(k)

    # order = Get the ASCII number of a character
    # 사용자가 누른 값 = q의 아스키 숫자라면 -> quit -> 모터를 정지시킨다
    if k == ord('q'):
        break


    # 사용자가 누른 값 = s의 아스키 숫자라면
    if k == ord('s'):

        # 정지 상태였을 경우 -> start
        if start_flag == False:
            start_flag = True

        # 가동 상태였을 경우 -> stop
        else:
            start_flag = False

        # 플래그 상태를 출력한다
        print('start_flag: ', start_flag)

    # 방금 start 상태로 바꾸었을 경우
    if start_flag == True:

        # up 키를 눌렀다면
        if k == 82:   #forward

            # 양쪽 모터를 20 속도로 움직인다
            hw.motor_one_speed(20)
            hw.motor_two_speed(20)

    # 방금 stop 상태로 바꾸었을 경우
    else:

        # 모터를 멈춘다
        hw.motor_one_speed(0)
        hw.motor_two_speed(0)


hw.motor_clean()
cv2.destroyAllWindows()