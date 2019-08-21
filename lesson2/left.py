import xhat as hw
import cv2

img = cv2.imread('images.png')
cv2.imshow('image',img)

start_flag = False
while (True):
    k = cv2.waitKey(5)
    if k!= -1:
        print(k)

    if k == ord('q'):
        break

    if k == ord('s'):
        if start_flag == False:
            start_flag = True
        else:
            start_flag = False
        print('start_flag: ', start_flag)

    if start_flag == True:
        if k == 82:   #forward
            hw.motor_one_speed(20)
            hw.motor_two_speed(20)

        if k == 81:   #left
            hw.motor_one_speed(65)
            hw.motor_two_speed(15)
    else:
        hw.motor_one_speed(0)
        hw.motor_two_speed(0)

hw.motor_clean()
cv2.destroyAllWindows()