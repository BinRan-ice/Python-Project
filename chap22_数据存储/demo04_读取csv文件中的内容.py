# coding:utf-8
import csv
with open("文件/student.csv",mode="r",encoding="utf-8",newline="") as file:
    #创建reader对象
    reader=csv.reader(file)
    for row in reader:
        print(row)