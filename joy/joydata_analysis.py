import scipy.misc

import random
import csv
#from mlxtend.preprocessing import one_hot
import numpy as np
import config as cfg

xs = []
ys = []

wheel0 = 0
wheel1 = 0
wheel2 = 0


#read data.csv
with open('joydata/' + cfg.currentDir + '/data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        #print(row[0], row[1])
        xs.append('joydata/' + cfg.currentDir + '/' + row[0])
        ys.append(int(row[1]))
        if int(row[1]) == 0:
            wheel0 += 1
        elif int(row[1]) > 0:
            wheel1 += 1
        elif int(row[1]) < 0:
            wheel2 += 1
        
print( '=======================================================')
print('Total data counts of data.csv: ', len(xs))
print('straight data counts: ', wheel0, ', ratio(%):', ' %0.1f' % (wheel0/len(xs)*100))
print('Right data counts: ', wheel1, ', ratio(%):', ' %0.1f' % (wheel1/len(xs)*100))
print('Left data counts: ', wheel2, ', ratio(%):', ' %0.1f' % (wheel2/len(xs)*100))

print( '-------------------------------------------------------')

xs = []
ys = []

wheel0 = 0
wheel1 = 0
wheel2 = 0


#read data.csv
with open('joydata/' + cfg.currentDir + '/dcdata.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        #print(row[0], row[1])
        xs.append('joydata/' + cfg.currentDir + '/' + row[0])
        ys.append(int(row[1]))
        if int(row[1]) == 0:
            wheel0 += 1
        elif int(row[1]) > 0:
            wheel1 += 1
        elif int(row[1]) < 0:
            wheel2 += 1
        

print('Total data counts of dcdata.csv: ', len(xs))
print('straight data counts: ', wheel0, ', ratio(%):', ' %0.1f' % (wheel0/len(xs)*100))
print('Right data counts: ', wheel1, ', ratio(%):', ' %0.1f' % (wheel1/len(xs)*100))
print('Left data counts: ', wheel2, ', ratio(%):', ' %0.1f' % (wheel2/len(xs)*100))
print( '=======================================================')
