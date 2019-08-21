import cv2


img = cv2.imread('images.png')

cv2.imshow('image',img)

while (True):
    k = cv2.waitKey(5)
    
    if k == ord('q'):
        break

cv2.destroyAllWindows()
