'''훈련데이터 분석 과정 1

좌회전, 우회전, 직진, 정지 데이터의 수량과 비율을 계산한다
'''


# SciPy: 과학기술계산을 위한 파이썬 라이브러리
# misc(=Miscellaneous routines): SciPy 패키지의 서브패키지
import scipy.misc

import random
import csv
#from mlxtend.preprocessing import one_hot
import numpy as np
import config as cfg


# xs: 이미지 경로를 담는 리스트
# ys: 이미지의 방향 값을 담는 리스트
xs = []
ys = []

wheel0 = 0
wheel1 = 0
wheel2 = 0
wheel3 = 0

#points to the end of the last batch --- 무슨 말??
train_batch_pointer = 0
val_batch_pointer = 0

#read data.csv
with open('data/' + cfg.currentDir + '/data.csv', newline='') as csvfile:

    # quotechar : 각 필드에서 값을 둘러싸고 있는 문자. 기본값: '"'
    # 나뉘면 안 되는 데이터를 quotechar로 묶어준다는 의미
    # ex) "Hello, python" 이라는 String을 '"' 단위로 묶어주므로, delimiter인 ','에 의해 Hello 와 python이 나뉘는 것을 막아준다
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        #print(row[0], row[1])
        xs.append('data/' + cfg.currentDir + '/' + row[0])
        ys.append(int(row[1]))
        if int(row[1]) == 0:
            wheel0 += 1
        elif int(row[1]) == 1:
            wheel1 += 1
        elif int(row[1]) == 2:
            wheel2 += 1
        elif int(row[1]) == 3:
            wheel3 += 1



# 좌회전, 우회전, 직진, 정지 데이터의 수량과 비율을 터미널에 출력한다
print('Total data counts: ', len(xs))
print('Stop data counts: ', wheel0, ', ratio(%):', ' %0.1f' % (wheel0/len(xs)*100))
print('Left data counts: ', wheel1, ', ratio(%):', ' %0.1f' % (wheel1/len(xs)*100))
print('strait data counts: ', wheel2, ', ratio(%):', ' %0.1f' % (wheel2/len(xs)*100))
print('Right data counts: ', wheel3, ', ratio(%):', ' %0.1f' % (wheel3/len(xs)*100))
##여기에 후진, 부스터 데이터도 추가해야 하나??


# 원 핫 인코딩: 문자를 숫자로 바꾸는 기법 중 하나 -- 이거 왜 하지?
###ys = one_hot(ys, num_labels=4, dtype='int')

#print(np.reshape(ys, -1))





'''
훈련데이터와 검증데이터를 나눈다

훈련 데이터(training data): 인공지능이 스스로 학습을 하는 데 사용하는 데이터
검증 데이터(validation data): 훈련 데이터를 통한 학습과 비교하는 용도로 활용하는 데이터. 인공지능이 직접 활용하지 않는다
훈련데이터:검증데이터 = 8:2
'''
#get number of images
num_images = len(xs)

#shuffle list of images
# list(zip(ooo)) : list를 여러 개로 slice 한다 - 같은 길이의 리스트를 같은 인덱스끼리 잘라서 리스트로 반환해준다
# ([x1, x2, x3...], [y1, y2, y3...]) => ([x1, y1], [x2, y2]...) 이렇게 바꾼다
c = list(zip(xs, ys))

# 원소의 순서를 랜덤하게 바꾼다
# ([x1, y1], [x2, y2]...) => ([x9, y9], [x3, y3]...)
random.shuffle(c)

# *: list를 unpack 한다. 원소를 개별 argument로 취급 -- ([x9, y9], [x3, y3]...) => [x9, y9], [x3, y3]...
# 리스트를 원래의 xs, ys 상태로 복귀시킨다
# ([x9, y9], [x3, y3]...) => (x9, x3...), (y9, y3..)
xs, ys = zip(*c)

# list 에서 int(len(xs) * 0.8) 번째 요소 직전까지 slice
# 훈련값 가운데, 앞의 80퍼센트에 해당하는 요소만 활용
train_xs = xs[:int(len(xs) * 0.8)]
train_ys = ys[:int(len(xs) * 0.8)]

# 맨 뒤에서부터 아이템 int(len(xs) * 0.2) 개를 가져온다
# 훈련값 가운데, 뒤의 20퍼센트에 해당하는 요소만 활용
val_xs = xs[-int(len(xs) * 0.2):]
val_ys = ys[-int(len(xs) * 0.2):]

"""
train_xs = xs[:int(len(xs) * 1)]
train_ys = ys[:int(len(xs) * 1)]

val_xs = xs[-int(len(xs) * 1):]
val_ys = ys[-int(len(xs) * 1):]
"""



num_train_images = len(train_xs)
num_val_images = len(val_xs)


# batch = 작업단위. 1 batch = 100개의 데이터(이미지)
# 특정 작업단위 까지의 훈련데이터를 가져온다 -- 분석용도?
def LoadTrainBatch(batch_size):
    global train_batch_pointer

    # 이게 뭐지?
    x_out = []
    y_out = []
    for i in range(0, batch_size):

        # batch에 해당하는 이미지를 resize해서 리스트에 담는다
        # imresize(imread(파일이름, rgb))
        x_out.append(scipy.misc.imresize(scipy.misc.imread(train_xs[(train_batch_pointer + i) % num_train_images])[cfg.modelheight:], [66, 200]) / 255.0)

        # batch에 해당하는 방향 값을 담는다
        y_out.append([train_ys[(train_batch_pointer + i) % num_train_images]])
    train_batch_pointer += batch_size
    return x_out, y_out


# 특정 작업단위 까지의 검증데이터를 가져온다 -- 분석용도?
def LoadValBatch(batch_size):
    global val_batch_pointer
    x_out = []
    y_out = []
    for i in range(0, batch_size):
        x_out.append(scipy.misc.imresize(scipy.misc.imread(val_xs[(val_batch_pointer + i) % num_val_images])[cfg.modelheight:], [66, 200]) / 255.0)
        y_out.append([val_ys[(val_batch_pointer + i) % num_val_images]])
    val_batch_pointer += batch_size
    return x_out, y_out

