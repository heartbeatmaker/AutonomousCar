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
            hw.motor_one_speed(50)
        else:
            start_flag = False
            hw.motor_one_speed(0)

        print('start_flag: ', start_flag)

hw.motor_clean()
cv2.destroyAllWindows()