import csv

 
# save data in csv file.

f=open('./data/test.csv','w')

# delimiter: 구획문자. 필드를 구분하는데 사용하는 한 문자. 기본값: "," (콤마)
# lineterminator: writer에 의해 생성된 행을 종료하는데 사용하는 문자열. 기본값: "\r\n"
fwriter = csv.writer(f, delimiter=";", lineterminator="\n")

fwriter.writerow((1, 'Hello World!!!'))

f.close()
