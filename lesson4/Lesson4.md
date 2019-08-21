Lesson4
학습내용
-	자율주행자동차 원리
-	자동차 시범 운전
-	자율주행자동차를 위한 훈련데이터 수집 
-	인공지능 훈련 및 검증

1.	자율주행자동차 차선유지 기능 구현 원리 설명
훈련데이터 수집 -> 훈련 -> 시뮬레이션 -> 테스트

2.	lesson4 로 폴더이동
cd /home/orangepi/autonomousCar/lesson4 또는 cd ../lesson4

3.	시범 운전하기
sudo python3 keyboard.py 

s: 운전모드/정지모드 토글방식
방향키로 직진/좌회전/우회전
q;  프로그램 종료
4.	훈련데이터 수집  및 정제
sudo python3 keyboard.py 

r: 데이터수집모드/데이터수정지모드 토글방식
방향키로 직진/좌회전/우회전
q;  프로그램 종료

5.	훈련데이터 분석
sudo python3 data_analysis.py

6.	좌우이미지 반전 데이터 만들기
sudo python3 decalcom.py

sudo python3 data_analysis.py 데이터 확인하기

7.	인공지능 훈련 및 관찰
sudo python3 train.py

터미널에서 아래 명령어 실행
tensorboard --logdir=./logs –port=6006
브라우져에서 아래 명령어 실행
localhost:6006

8.	시뮬레이션
sudo python3 simulate.py

9.	테스트
sudo python3 airun.py

10.	정리하기
