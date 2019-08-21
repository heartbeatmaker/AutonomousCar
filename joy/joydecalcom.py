import scipy.misc
import cv2
import random
import csv
#from mlxtend.preprocessing import one_hot
import numpy as np
import config as cfg

x1 = []
#y1 = []
x2 = []
x3 = []
#y3 = []


#delete dc_img* in data.csv file
originalrows = []
with open('joydata/' + cfg.currentDir + '/data.csv', newline='') as csvfile:
    filereader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in filereader:
        #print(row[0], row[1])
        if row[0][:2] != 'dc':
            originalrows.append(row)

with open('joydata/' + cfg.currentDir + '/data.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|')
    filewriter.writerows(originalrows)


cfg.f=open(cfg.outputDir+cfg.currentDir+'/dcdata.csv','w')
cfg.fwriter = csv.writer(cfg.f)

#read data.csv
with open('joydata/' + cfg.currentDir + '/data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    cfg.fwriter.writerows(originalrows)

    for row in spamreader:
        #print(row[0], row[1])
        full_image = cv2.imread('joydata/' + cfg.currentDir + '/' + row[0] , cv2.IMREAD_COLOR)
        full_image = cv2.flip(full_image, 1)
        myfile = 'joydata/' + cfg.currentDir + '/dc_' + row[0]
        cv2.imwrite(myfile,full_image)

        if int(row[1]) >= 0:
            cfg.fwriter.writerow(('dc_' + row[0], '-' + row[1]))
        if int(row[1]) < 0:
            cfg.fwriter.writerow(('dc_' + row[0], int(row[1])* (-1)))    
        

