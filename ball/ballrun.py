import numpy as np
import cv2
import imutils
import time
import config as cfg
import xhat as hw

# define the lower and upper boundaries of the "green"
# ball in the HSV color space, then initialize the
# list of tracked points
greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)

start_flag = False
normal_speed = 40   ###60
tempV = 0
overV = 0
ball_flag = False

vs = cv2.VideoCapture(0)
vs.set(cv2.CAP_PROP_FRAME_WIDTH, cfg.width)
vs.set(cv2.CAP_PROP_FRAME_HEIGHT, cfg.height)
#vs.set(cv2.CAP_PROP_FPS, 15)

# allow the camera or video file to warm up
time.sleep(2.0)

# keep looping
while (True):
	# grab the current frame
	_, frame = vs.read()

	# handle the frame from VideoCapture or VideoStream
	#frame = frame[1] if args.get("video", False) else frame

	# if we are viewing a video and we did not grab a frame,
	# then we have reached the end of the video
	if frame is None:
		print('There is no camera.')
		break

	# blur it, and convert it to the HSV
	# color space

	###blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	###hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# construct a mask for the color "green", then perform
	# a series of dilations and erosions to remove any small
	# blobs left in the mask
	mask = cv2.inRange(hsv, greenLower, greenUpper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)

	# find contours in the mask and initialize the current
	# (x, y) center of the ball
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	center = None

	# only proceed if at least one contour was found
	if len(cnts) > 0:
		
		# find the largest contour in the mask, then use
		# it to compute the minimum enclosing circle and
		# centroid
		c = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

		# only proceed if the radius meets a minimum size
		if radius > 20 :  ###10:
			ball_flag = True
			# draw the circle and centroid on the frame,
			# then update the list of tracked points
			cv2.circle(frame, (int(x), int(y)), int(radius),
				(0, 255, 255), 2)
			#cv2.circle(frame, center, 5, (0, 0, 255), -1)
		else:
			ball_flag = False

	print('ball_flag: ', ball_flag)

	if ball_flag:
		cfg.joyX = int((x-160)/160*100)  #int(degree * 100)
	else:
		cfg.joyX = 0

	# show the frame to our screen
	cv2.imshow("Frame", frame)
	k = cv2.waitKey(1) & 0xFF

	# if the 'q' key is pressed, stop the loop
	if k == ord("q"):
		break

	if k == ord('s'):  #k == 115: #115:'s'
		if start_flag == False: 
			start_flag = True
		else:
			start_flag = False
		print('start flag:',start_flag)


	if start_flag and ball_flag:
		if cfg.joyX > 100:
			cfg.joyX = 100
		if cfg.joyX < -100:
			cfg.joyX = -100

		if cfg.joyX < 0:
			tempV = normal_speed - cfg.joyX
		else:
			tempV = normal_speed + cfg.joyX

		if tempV <= 100:
			overV = 0
		else:
			overV = tempV - 100
			tempV = 100

		if cfg.joyX < 0:
			hw.motor_two_speed(normal_speed - overV)
			hw.motor_one_speed(tempV)
		else:
			hw.motor_two_speed(tempV)
			hw.motor_one_speed(normal_speed - overV)
	else:
		hw.motor_one_speed(0)
		hw.motor_two_speed(0)
		cfg.joyX = 0


###c.release() 
hw.motor_clean()
# close all windows
cv2.destroyAllWindows()

