import csv
 
# save data in csv file.
f=open('./data/test.csv','w')
fwriter = csv.writer(f)

for i in range(1,10):
    fwriter.writerow((i, 'Hello World!!!'))

f.close()

