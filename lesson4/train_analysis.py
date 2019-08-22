
'''
TensorFlow: 구글에서 만든, 딥러닝 프로그램을 쉽게 구현할 수 있도록 다양한 기능을 제공해주는 라이브러리
기본적으로 C++로 구현 되어 있으며, Python, Java, Go 등 다양한 언어를 지원
파이썬을 최우선으로 지원하며, 대부분의 편한 기능들이 파이썬 라이브러리로만 구현되어 있어 Python에서 개발하는 것이 편함

텐서: 연산의 모음

*텐서보드: 시각화 도구
- 학습하는 중간중간 손실값이나 정확도 또는 결과물로 나온 이미지나 사운드 파일들을 다양한 방식으로 시각화해 보여준다
- 딥러닝 학습 과정을 추적하는 데 유용하다
- 사용법: 콘솔로 실행하고, 브라우저에서 화면을 볼 수 있다

* 텐서보드, 왜 사용하나?
- 학습과정에서 개발자가 보고싶은 정보들을 '실시간으로 이미지화'할 수 있다

일일이 로그로 찍어서 터미널에서 확인할 수도 있다. 그러나 이것은 불편하다
기존의 학습내용과 비교분석이 가능하다
실시간으로 결과를 이미지화 할 수 있다

'''

import tensorflow as tf
import scipy.misc
import model
import cv2
from subprocess import call
import time
import csv
import numpy as np
import config as cfg

sess = tf.InteractiveSession()
saver = tf.train.Saver()
saver.restore(sess, "save/model.ckpt")

# img = cv2.imread('steering_wheel_image.jpg',0)
# rows,cols = img.shape

smoothed_angle = 0

xs = []
ys = []

with open(cfg.outputDir+cfg.currentDir+'/data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        #print(row[0], row[1])
        xs.append(row[0])
        ys.append(row[1])

print(len(ys))
total_num = len(ys)

i = 0
correct_num = 0
left_num = 0
forward_num = 0
right_num = 0
correct_left = 0
correct_right = 0
correct_forward = 0

while(True):
    full_image = scipy.misc.imread('data/' + cfg.currentDir + '/' + xs[i] , mode="RGB")
    image = scipy.misc.imresize(full_image[cfg.modelheight:], [66, 200]) / 255.0
    
    degrees = model.y.eval(feed_dict={model.x: [image], model.keep_prob: 1.0})

    if int(ys[i]) == np.argmax(degrees, axis=1):
        correct_num += 1

    if int(ys[i]) == 1:
        left_num += 1
        if int(ys[i]) == np.argmax(degrees, axis=1):
            correct_left += 1

    if int(ys[i]) == 2:
        forward_num += 1
        if int(ys[i]) == np.argmax(degrees, axis=1):
            correct_forward += 1

    if int(ys[i]) == 3:
        right_num += 1
        if int(ys[i]) == np.argmax(degrees, axis=1):
            correct_right += 1



    i += 1

    if total_num == i:
        break

print('i:', i, 'correct_num: ', correct_num, 'percentage: ', correct_num/(i) * 100)
    
    
if left_num != 0:
    print('left_num: ', left_num, 'correct_left: ', correct_left, 'percentage: %0.1f' % (correct_left/left_num*100) )

if forward_num != 0:
    print('forward_num: ', forward_num, 'correct_forward: ', correct_forward, 'percentage: %0.1f' % (correct_forward/forward_num*100) )

if right_num != 0:
    print('right_num: ', right_num, 'correct_right: ', correct_right, 'percentage: %0.1f' % (correct_right/right_num*100) )

