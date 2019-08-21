Lesson3

<pi camera 실습>
파이카메라를 활용하여 인공지능 훈련데이터 수집 준비하기
학습목표
-	파이카메라 특징 이해하기
-	카메라 세팅 방법 이해하기
-	연속적인 화면 재생과 화면 캡쳐 방법 배우기

      1.   lesson3 으로 작업폴더 변경
cd /home/orangepi/autonomousCar/lesson3 

      2.   csv 파일에 데이터 저장하기
python3 savedata1.py

/home/orangepi/autonomousCar/lesson3/data/test.csv 파일을 열어서 확인

      3.   csv 파일에 연속적인 데이터 저장하기
python3 savedata2.py

            /home/orangepi/autonomousCar/lesson3/data/test.csv 파일을 열어서 확인

      4.  연속적인 화면 재생
python3 capture1.py


      5.  현속적인 화면 캡쳐하기
python3 capture2.py

/home/orangepi/autonomousCar/lesson3/data 폴더에 이미지가 연속적으로 저장됩니다. 

      6.  캡쳐된 이미지 정보 리스트 만들기
python3 capture3.py

/home/orangepi/autonomousCar/lesson3/data 폴더에 이미지가 연속적으로 저장됩니다. 캡쳐된 이미지 리스트는 data.csv 파일에 리스트 형식으로 저장됩니다.

