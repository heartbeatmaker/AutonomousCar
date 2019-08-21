import xhat as hw

# range(시작숫자, 종료숫자, step)
# 시작숫자, step은 생략 가능

# ex) list(range(10, 15))
# = [10,11,12,13,14]
#
# list(range(10,20,3))
# = [10,13,16,19]


# 0~99 까지 아래의 절차를 반복한다
for i in range(100):
    # 들여쓰기를 꼭 해야한다
    hw.motor_one_speed(50)

hw.motor_clean()