# 모터 구동 속도 변경 실습

import xhat as hw

print('Press ctrl + c to terminate program')
while(True):
    hw.motor_one_speed(50)


hw.motor_clean()