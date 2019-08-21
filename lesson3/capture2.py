import time
import cv2

c = cv2.VideoCapture(0) 
time.sleep(0.1)
 

cnt = 0
while(True):
    _,image = c.read()

    # show the frame
    cv2.imshow("Frame", image)

    myimage = './data/'+ time.strftime('%Y-%m-%d_%H:%M:%S') \
                  +'_' + str(cnt) + '.jpg'
    cv2.imwrite(myimage, image)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

    cnt += 1	

cv2.destroyAllWindows()