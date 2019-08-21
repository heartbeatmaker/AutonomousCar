# -*- coding: utf-8 -*-


# Configuration
width = 320  #464  #455 # Video width requested from camera
height = 240  #256 # Video height requested from camera
pi_hflip = True # Flip Picamera image horizontally
pi_vflip = True # Flip Picamera image vertically


left_motor = 0
right_motor = 0
wheel = 0  #0:stop, 1:left, 2:strait, 3:right
joyX = 0

recording = False

cnt = 0
outputDir = '/home/orangepi/autonomousCar/joy/joydata/'
currentDir = 'training' 
file = ""
f = ''
fwriter = ''
joyX = 0
frame = ''

Voicecontrol = False

AIcontrol = False
modelheight = -130  ###-150 ###-160 ###-130 ###-150 #-115 #-130 #-150 #-250 #-200

# training speed setting(30,15), (45,20)
#car_model2-rpm200-motor: (80, 10, 25)
maxturn_speed = 60
minturn_speed = 10  ###20  ###15
normal_speed_left = 30
normal_speed_right = 30
wheel_alignment_left = 0
wheel_alignment_right = 0



# testing speed setting(
ai_maxturn_speed = 90
ai_minturn_speed = 15
ai_normal_speed_left = 70
ai_normal_speed_right = 70




