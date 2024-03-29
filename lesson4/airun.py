import xhat as hw
import time
import cv2
import config as cfg
#import opidistance3 as dc
import tensorflow as tf
import scipy.misc
import numpy as np
import model

import os
import sys
import signal
import csv


'''
if __name__ == '__main__' 쓰는 이유?

파이썬은 자동으로 실행되는 메인함수가 없다
파이썬은 메인 함수가 없는 대신 들여쓰기 하지 않은 모든 코드(level 0코드)를 실행한다
(정의된 함수나 클래스는 실행x)

__name__은 현재 모듈의 이름을 담고있는 내장 변수이다
python myscript.py 같이 이 모듈이 '직접 실행되는 경우'에만,__name__ 은 "__main__"으로 설정된다

myscript.py의 코드가 다른 모듈에 의해 import된 경우, 함수와 객체의 정의는 import되지만, 
__name__이 "__main__"이 아니기 때문에 if문은 실행되지 않는다

==> 직접 실행할 때와 import해서 실행할 때를 구분해준다
'''

if __name__ == '__main__':


    sess = tf.InteractiveSession()
    saver = tf.train.Saver()
    saver.restore(sess, "save/model.ckpt")

    start_flag = False

    #testing speed variation
    speed_change_flag = False

    if speed_change_flag:
        cfg.maxturn_speed = cfg.ai_maxturn_speed
        cfg.minturn_speed = cfg.ai_minturn_speed
        cfg.normal_speed_left = cfg.ai_normal_speed_left
        cfg.normal_speed_right = cfg.ai_normal_speed_right
    
    c = cv2.VideoCapture(0)
    c.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    c.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
    #c.set(cv2.CAP_PROP_FPS, 15)

    while(True):
        _,full_image = c.read()
        #full_image = cv2.resize(full_image, (320,240))
        image = scipy.misc.imresize(full_image[cfg.modelheight:], [66, 200]) / 255.0
        image1 = scipy.misc.imresize(full_image[cfg.modelheight:], [66*2, 200*2])

        #cv2.imshow('original',full_image)
        #cv2.imshow("view of AI", cv2.cvtColor(image1, cv2.COLOR_RGB2BGR))
        cv2.imshow("view of AI", image1)


        wheel = model.y.eval(session=sess,feed_dict={model.x: [image], model.keep_prob: 1.0})
        cfg.wheel = np.argmax(wheel, axis=1)
        #print('wheel value:', cfg.wheel, wheel)
        print('wheel value:', cfg.wheel, model.softmax(wheel))

    
        k = cv2.waitKey(5)
        if k == ord('q'):  #'q' key to stop program
            break

        """ Toggle Start/Stop motor movement """
        if k == ord('a'): 
            if start_flag == False: 
                start_flag = True
            else:
                start_flag = False
            print('start flag:',start_flag)
   
        #to avoid collision when ultrasonic sensor is available
        length = 30 #dc.get_distance()
        if  5 < length and length < 15 and start_flag:
            hw.motor_one_speed(0)
            hw.motor_two_speed(0)
            print('Stop to avoid collision')
            time.sleep(0.5)
            continue
        
        if start_flag:
            if cfg.wheel == 0:
                hw.motor_two_speed(0)
                hw.motor_one_speed(0)

            if cfg.wheel == 1:   #left turn
                hw.motor_two_speed(cfg.minturn_speed)
                hw.motor_one_speed(cfg.maxturn_speed)
            

            if cfg.wheel == 2:
                hw.motor_two_speed(cfg.normal_speed_left)
                hw.motor_one_speed(cfg.normal_speed_right)

            if cfg.wheel == 3:   #right turn
                hw.motor_two_speed(cfg.maxturn_speed)
                hw.motor_one_speed(cfg.minturn_speed)
        
        else:
            hw.motor_one_speed(0)
            hw.motor_two_speed(0)
            cfg.wheel = 0

        
hw.motor_clean()
cv2.destroyAllWindows()
