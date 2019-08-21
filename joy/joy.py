#!/usr/bin/env python
from __future__ import division
import os
import sys
import signal
import threading
import time
import json
from flask import Flask, request, Response
from gevent.pywsgi import WSGIServer
import xhat as hw
import config as cfg
import camera as cam
import cv2
import csv

app = Flask(__name__, static_url_path='/static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Base URL / - loads web interface        
@app.route('/')
def index():
    
    return app.send_static_file('gear.html')
    #return app.send_static_file('default.html')

def gen(camera):
    """Video streaming generator function."""
    if cfg.camera_detected:
        #while True:
        #    cfg.frame = camera.get_frame()
        """
        while True:
            frame = camera.get_frame()
            cv2.resize(frame, (320,240))
            cv2.imshow('frame',frame)
            k = cv2.waitKey(5)
            #print(k)
            if k == ord('q'):  #'q' key to stop program
                break
            #yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        cv2.destroyAllWindows()
        """
        return camera.get_frame()

def saveimage():
    if cfg.recording:
        myfile = 'img_'+time.strftime('%Y-%m-%d_%H-%M-%S')+'_'+str(cfg.cnt)+'.jpg'
        #print(myfile, cfg.joyX)

        cfg.fwriter.writerow((myfile, cfg.joyX))

        cv2.imwrite(cfg.outputDir+cfg.currentDir+'/'+ myfile, cfg.frame)

        cfg.cnt += 1

# URL for motor control - format: /motor?l=[speed]&r=[speed]
@app.route('/motor')
def motor():
    left = request.args.get('l')
    right = request.args.get('r')
    cfg.joyX = request.args.get('joyX')
    recording = request.args.get('record')

    #print(recording)
    
    if cfg.camera_detected:
        cfg.frame = gen(cam.Camera())
        #cv2.imwrite(cfg.outputDir+cfg.currentDir+'/'+ 'test.jpg', cfg.frame)
    

    if recording == 'Y':
        #cfg.frame = gen(cam.Camera())
        #cv2.imwrite(cfg.outputDir+cfg.currentDir+'/'+ 'test.jpg', cfg.frame)

        cfg.recording = True
        #if cfg.cnt == 0:
        cfg.f=open(cfg.outputDir+cfg.currentDir+'/data.csv','a')
        cfg.fwriter = csv.writer(cfg.f)
        
        saveimage()

    if recording == 'N':
        cfg.recording = False
        cfg.cnt = 0
        if cfg.f != '':
            cfg.f.close()

    if left :
        left = int(left)
        if left >= -100 and left <= 100:
            cfg.left_motor = left
            hw.motor_two_speed(cfg.left_motor)
    if right:
        right = int(right)
        if right >= -100 and right <= 100:
            cfg.right_motor = right
            hw.motor_one_speed(cfg.right_motor)
    return 'ok'


# URL for video stream feed
@app.route('/record')
def record():
    left = request.args.get('l')
    right = request.args.get('r')
    print(left,right)
    if cfg.camera_detected:
        """Video streaming route. Put this in the src attribute of an img tag."""
        #return Response(gen(cam.Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')
        #frame = gen(cam.Camera())
        #frame = gen(cam.Camera())
        
        #while True:
        cfg.frame = gen(cam.Camera())
        if left :
            left = int(left)
            if left >= -100 and left <= 100:
                cfg.left_motor = left
                hw.motor_two_speed(cfg.left_motor)
        if right:
            right = int(right)
            if right >= -100 and right <= 100:
                cfg.right_motor = right
                hw.motor_one_speed(cfg.right_motor)
        
        return 'record_ok'
    else:
        return 'no video'
        




        

if __name__ == '__main__':

    cfg.camera_detected, cfg.camera_handle = cam.init_camera()
    #gen(cam.Camera())
    
    #cfg.frame = gen(cam.Camera())
    #cv2.imwrite(cfg.outputDir+cfg.currentDir+'/'+ 'test.jpg', cfg.frame)

    
    #cam.Camera()
    #print('camera started')
    #app.run(host='0.0.0.0', debug=False, threaded=True)
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()

    
hw.motor_clean()
cv2.destroyAllWindows()