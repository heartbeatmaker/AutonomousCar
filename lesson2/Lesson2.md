Lesson2
학습내용
-	자판의 키값을 받아 처리하는 방법
-	토글키에 대한 이해
-	방향키를 통한 자동차 직진, 좌회전, 우회전 제어
-	

cd /home/orangepi/autonomousCar/lesson2 또는 cd ../lesson2

1.	키 값을 입력 받기 위한 환경에 대한 이해
python3 key1.py


실행되면 이미지창이 뜹니다. 키보드에서 아무키나 누르면 종료가 됩니다.

2.	키 값을 받을 때까지 기다리며 ‘q’값이 입력되면 종료되는 예
python3 key2.py

a,b,c 등 아무키를 눌렀을 때 반응확인하기
q를 입력했을 때 반응확인하기

3.	활동하기
s를 입력했을 때 ‘Start’ 라고 프린터하기

python3 key3.py

s를 한번 누르면 ‘Start’ 다시 한번 누르면 ‘Stop’이 되는 토글키 구현하기
python3 key4.py

s를 누르면 모터를 구동하고 다시 s를 누르면 모터를 정지하기
sudo python3 key_motor1.py

s를 누르면 모터 조작을 활성화하고 다시 s를 누르면 모터 정지하기
모터 조작은 ↑방향키로 함
sudo python3 key_motor2.py

4.	화살표 키 값을 통해 모터 제어하기
직진: 양쪽 모터를 같은 속도로 구동하면 됨
sudo python3 forward.py

모터 조작은  위쪽(↑)방향키로 함

 
좌회전: 
sudo python3 left.py

모터 조작은  왼쪽(←) 방향키로 함

우회전:
sudo python3 right.py

모터 조작은 오른쪽(→) 방향키로 함

종합하기:
직진, 좌회전, 우회전을 모두 구현하여 키보드로 조종해 보자
sudo python3 run.py


5.	정리하기
#키 값을 받는 방법에 대해서 배웠습니다.
#토글키의 작동 방식에 대해 배웠습니다.
#키값을 통해 직진, 좌회전, 우회전하는 것을 배웠습니다.
