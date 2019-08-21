import time
import cv2

# CSV = Comma-separated values ; 각 라인의 컬럼들이 콤마로 분리된 텍스트 파일 포맷
# csv 파일을 읽기 위해서는 파이썬에 기본 내장된 csv 모듈을 import 해야 한다
import csv

# 내장카메라 or 외장카메라에서 영상을 받아온다
# 0 = 카메라의 장치번호. 노트북에서 내장카메라는 장치번호가 0이다
# 카메라를 추가연결하여 외장카메라를 사용하는 경우, 장치번호가 1~n까지 변화한다
c = cv2.VideoCapture(0)
time.sleep(0.1)
 
# capture frames from the camera
cnt = 0

# 파일 객체 = open(파일 이름, 파일 열기 모드)
# 파일 열기 모드 종류: r(읽기), w(쓰기), a(추가; append)

# .csv 파일을 쓰기 모드로 오픈한다
f=open('./data/data.csv','w')

# 파일 객체를 csv.writer라는 파일객체에 넣는다
fwriter = csv.writer(f)

while(True):
    _,image = c.read()
    image = cv2.resize(image, (320,240))

    # show the frame
    cv2.imshow("Frame", image)

    myimage = time.strftime('%Y-%m-%d_%H:%M:%S') +'_' + str(cnt) + '.jpg'
    cv2.imwrite('./data/'+ myimage, image)

    # csv 파일에 list 데이터를 한 라인 추가한다
    fwriter.writerow((myimage, 1))

    key = cv2.waitKey(1)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

    cnt += 1

# 열려 있는 파일 객체를 닫는다
f.close()
cv2.destroyAllWindows()