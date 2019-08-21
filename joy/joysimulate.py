import tensorflow as tf
import scipy.misc
import joymodel as model
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

print(xs[0])

i = 0
correct_num = 0
while(cv2.waitKey(10) != ord('q')):
    ###full_image = scipy.misc.imread("driving_dataset/" + str(i) + ".jpg", mode="RGB")
    full_image = scipy.misc.imread('joydata/' + cfg.currentDir + '/' + xs[i] , mode="RGB")
    #full_image = scipy.misc.imread(xs[i] , mode="RGB")
    image = scipy.misc.imresize(full_image[cfg.modelheight:], [66, 200]) / 255.0
    
    image1 = scipy.misc.imresize(full_image[cfg.modelheight:], [66*3, 200*3])
    
    ###degrees = model.y.eval(feed_dict={model.x: [image], model.keep_prob: 1.0})[0][0] * 180.0 / scipy.pi
    degrees = model.y.eval(feed_dict={model.x: [image], model.keep_prob: 1.0})
    ###call("clear")
    print("Label y: " + ys[i], 'prediced value:', int(degrees *100))
    ###cv2.imshow("frame", cv2.cvtColor(full_image, cv2.COLOR_RGB2BGR))
    cv2.imshow("Feed", cv2.cvtColor(image1, cv2.COLOR_RGB2BGR))
    cv2.imshow("Original", cv2.cvtColor(full_image, cv2.COLOR_RGB2BGR))

    #make smooth angle transitions by turning the steering wheel based on the difference of the current angle
    #and the predicted angle
    # smoothed_angle += 0.2 * pow(abs((degrees - smoothed_angle)), 2.0 / 3.0) * (degrees - smoothed_angle) / abs(degrees - smoothed_angle)
    # M = cv2.getRotationMatrix2D((cols/2,rows/2),-smoothed_angle,1)
    # dst = cv2.warpAffine(img,M,(cols,rows))
    # cv2.imshow("steering wheel", dst)

    #if int(ys[i]) == np.argmax(degrees, axis=1):
    #    correct_num += 1

    i += 1
    #print('i:', i, 'correct_num: ', correct_num, 'percentage: ', correct_num/(i) * 100)
    
    #time.sleep(1)

cv2.destroyAllWindows()