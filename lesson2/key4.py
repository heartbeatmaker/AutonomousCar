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
            print('Start!!!')
            start_flag = True
        else:
            print('Stop!!!')
            start_flag = False

cv2.destroyAllWindows()