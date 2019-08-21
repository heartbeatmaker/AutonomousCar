import xhat as hw
import time
import cv2
import config as cfg

import tensorflow as tf
import scipy.misc
import numpy as np
import joymodel as model

import os
import sys
import signal
import csv

def recording():
    if cfg.recording:
        cfg.recording = False
        cfg.f.close()
    else:
        cfg.recording = True
        if cfg.currentDir == '':
            cfg.currentDir = time.strftime('%Y-%m-%d')
            os.mkdir(cfg.outputDir+cfg.currentDir)
            cfg.f=open(cfg.outputDir+cfg.currentDir+'/data.csv','w')
        else:
            cfg.f=open(cfg.outputDir+cfg.currentDir+'/data.csv','a')
        cfg.fwriter = csv.writer(cfg.f)

def saveimage():
    if cfg.recording:
        myfile = 'img_'+time.strftime('%Y-%m-%d_%H-%M-%S')+'_'+str(cfg.cnt)+'.jpg'
        print(myfile, cfg.wheel)

        cfg.fwriter.writerow((myfile, cfg.wheel))

        cv2.imwrite(cfg.outputDir+cfg.currentDir+'/'+ myfile,full_image)

        cfg.cnt += 1

        


if __name__ == '__main__':
    sess = tf.InteractiveSession()
    saver = tf.train.Saver()
    saver.restore(sess, "save/model.ckpt")

    start_flag = False
    normal_speed = 25   ###40
    if normal_speed > 50:
        normal_speed = 50
    tempV = 0
    overV = 0

    #testing speed variation
    speed_change_flag = False

    if speed_change_flag:
        cfg.maxturn_speed = cfg.ai_maxturn_speed
        cfg.minturn_speed = cfg.ai_minturn_speed
        cfg.normal_speed_left = cfg.ai_normal_speed_left
        cfg.normal_speed_right = cfg.ai_normal_speed_right
    
    c = cv2.VideoCapture(0)
    c.set(cv2.CAP_PROP_FRAME_WIDTH, cfg.width)
    c.set(cv2.CAP_PROP_FRAME_HEIGHT, cfg.height)

    while(True):
        _,full_image = c.read()
        #full_image = cv2.resize(full_image, (320,240))
        image = scipy.misc.imresize(full_image[cfg.modelheight:], [66, 200]) / 255.0
        image1 = scipy.misc.imresize(full_image[cfg.modelheight:], [66*2, 200*2])

        #cv2.imshow('original',full_image)
        ###cv2.imshow("view of AI", cv2.cvtColor(image1, cv2.COLOR_RGB2BGR))
        cv2.imshow("view of AI", image1)

        degree = model.y.eval(session=sess,feed_dict={model.x: [image], model.keep_prob: 1.0})
        joyX = int(degree * 100)
        
        cfg.joyX = joyX

        print('joyX value:', cfg.joyX)

    
        k = cv2.waitKey(5)
        if k == ord('q'):  #'q' key to stop program
            break

        """ Toggle Start/Stop motor movement """
        if k == ord('a'):  #k == 115: #115:'s'
            if start_flag == False: 
                start_flag = True
            else:
                start_flag = False
            print('start flag:',start_flag)

        """ Toggle Record On/Off  """
        if k == 114: #114:'r'
            recording()
            if cfg.recording:
               start_flag = True
            else:
               start_flag = False
               cfg.cnt = 0
            print('cfg.recording:',cfg.recording)

        #save image files and images list file   
        if cfg.recording:
            saveimage()
            print(cfg.cnt)

        #avoid collision
        length = 30 #dc.get_distance()
        if  5 < length and length < 15 and start_flag:
            hw.motor_one_speed(0)
            hw.motor_two_speed(0)
            print('Stop to avoid collision')
            time.sleep(0.5)
            continue
        
        if start_flag:
            if cfg.joyX > 100:
                cfg.joyX = 100
            if cfg.joyX < -100:
                cfg.joyX = -100

            if cfg.joyX < 0:
                hw.motor_two_speed(normal_speed - int(normal_speed*(-cfg.joyX)/100))
                hw.motor_one_speed(normal_speed + int(normal_speed*(-cfg.joyX)/100))
            else:
                hw.motor_two_speed(normal_speed + int(normal_speed*cfg.joyX/100))
                hw.motor_one_speed(normal_speed - int(normal_speed*cfg.joyX/100))
        else:
            hw.motor_one_speed(0)
            hw.motor_two_speed(0)
            cfg.joyX = 0

        
hw.motor_clean()
cv2.destroyAllWindows()
