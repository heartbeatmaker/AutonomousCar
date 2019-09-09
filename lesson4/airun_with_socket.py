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

import socket
import threading

from etc.client import client

import requests




def clientAcceptingThread():
    while 1:
        client_socket, addr = server_socket.accept()
        print("connected client : ", addr[0], addr[1])

        client_socket_list.append(client(client_socket, addr[0]))
        print("number of clients : "+str(len(client_socket_list)))


def send_message(message):
    for i in client_socket_list:
        print("sending message ("+message+") to "+i.ip)
        i.send_msg(message)




if __name__ == '__main__':

    client_socket_list = list()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.0.77', 8999))
    server_socket.listen(0)
    print("Listening on 8999")

    t = threading.Thread(target = clientAcceptingThread)
    t.start()


    sess = tf.InteractiveSession()
    print("1")
    saver = tf.train.Saver()
    print("2")

    saver.restore(sess, "save/model.ckpt")
    print("3")

    start_flag = False
    print("4")


    #testing speed variation
    speed_change_flag = False
    print("5")

    if speed_change_flag:
        print("6")
        cfg.maxturn_speed = cfg.ai_maxturn_speed
        cfg.minturn_speed = cfg.ai_minturn_speed
        cfg.normal_speed_left = cfg.ai_normal_speed_left
        cfg.normal_speed_right = cfg.ai_normal_speed_right

    print("7")
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
                t = threading.Thread(target=send_message, args=("on",))
                r = requests.get("http://18.220.168.16/state_run.php")  # 앱에 주행중 표시
            else:
                start_flag = False
                t = threading.Thread(target=send_message, args=("off",))
                r = requests.get("http://18.220.168.16/state_stop.php")
            print('start flag:',start_flag)
            t.start()

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


