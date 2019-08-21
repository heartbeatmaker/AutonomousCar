import xhat as hw

# 모터 1의 속도를 50으로 둔다. speed는 마이너스도 가능. 실행 중 ctrl + c를 누르면 모터가 정지된다
hw.motor_one_speed(50)


# 모터를 멈추고, 입출력 연결을 해제한다
# cleanup all GPIO connections used in event of error by lib user
hw.motor_clean()