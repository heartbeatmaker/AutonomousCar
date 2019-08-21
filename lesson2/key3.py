import cv2

img = cv2.imread('images.png')

cv2.imshow('image',img)

while (True):
    k = cv2.waitKey(5)

    if k!= -1:
        print(k)

    if k == ord('q'):
        break

    if k == ord('s'):
        print('Start!!!')

cv2.destroyAllWindows()