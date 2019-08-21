Lesson1
학습내용
-	오렌지파이 부팅
-	오렌지파이 리눅스OS 환경 
-	파이썬 기본적인 사용법
-	모터 구동법

1.	<개발환경 준비하기>
준비물: 오렌지파이, 파워선, 마이크로SD, (키보드, 마우스, 모니터)
-	microSD card를 오렌파이에 삽입
-	오렌지파이와 모니터, 키보드, 마우스 연결(원격터미널 연결 시에는 생략)
-	오렌지파이 usb파워선 연결

*** 원격터미널 연결 시에는 컴퓨터에 VNC 프로그램 설치해야 함
2.	리눅스 OS 암비언 
-	메뉴 설명
-	와이파이 연결
-	(옵션)블루투스 키보드/마우스 연결

#전체폴더 구조 간략 설명

#터미널 사용법
cd: 폴더이동. 절대경로, 상대경로
pwd: 현재 폴더 
‘No such file or directory’ 메시지의 의미는?
	오타가 났을 때 발생하며, 오타를 수정해서 실행하면 됨

#text editor 사용법
새파일만들기, 저장하기, 파일명 변경하기, 다른 이름으로 저장하기

3.	파이썬 기본 내용 배우기

cd /home/orangepi/autonomousCar/lesson1

      #python 실행 및 종료
      버전2:python 소스파일명.py , 버전3: python3 소스파일명.py
      
#print 명령어를 실행/자동종료
print.py 파일을 텍스트에디터로 열어서 내용확인하기
python3 print.py

#순차 
python3 print_many.py

      #반복문
python3 print_for.py

python3 print_for2.py


4.	모터 구동 실습
준비물: 모터드라이브, 카메라연결선, 모터, 바퀴, 모터연결전선
<조립하기>
(1)	오렌지파이 종료 및 USB파워연결선 해체여부 확인
(2)	오렌지파이와 카메라 연결선 연결
(3)	모터드라이브 오렌지파이 연결
(4)	모터와 바퀴연결
(5)	모터와 모터드라이브 연결전선으로 연결
*** 주의사항: 조립은 반드시 오렌지파이의 USB파워선을 뽑은 상태로 진행해야 합니다. 감전이나 오렌지파이 파손을 예방하기 위함입니다.

#import 설명: 외부 라이브러리 및 함수 설명

#모터드라이브관련 라이브러리는 관리자권한이 필요합니다. 관리자모드로 실행하는 방법은 sudo 를 앞에붙이면 됩니다. 패스워드를  요구하면  orangepi   를  입력합니다.
sudo python3 motor1.py

sudo python3 motor_for1.py

sudo python3 motor_for2.py

#while 구문의 실행 및 비정상 종료
sudo python3 motor_while.py
비정상 종료: 실행 중 Ctrl + c  키입력

# motor_while.py 수정해서 모터 구동 속도 변경 실습
hw.motor_one_speed(0)
hw.motor_one_speed(50)
hw.motor_one_speed(100)
hw.motor_one_speed(200)

# motor_while.py 수정해서 모터 반대로 돌리기 실습
hw.motor_one_speed(-90) -> hw.motor_one_speed(90)
또는 hw.motor_one_speed(90) -> hw.motor_one_speed(-90)

# 모터드라이브와 모터연결선을 바꾸었을 때 모터 방향이 바뀌는 것 실습

