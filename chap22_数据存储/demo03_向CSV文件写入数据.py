# coding:utf-8
import csv

with open('文件/student.csv',mode="a+",encoding="utf-8",newline="") as file:
    #创建一个writer对象
    writer=csv.writer(file)
    #一次写一行数据
    writer.writerow(['李四',23,90])
    #一次写入多行数据
    lst=[
        ["Jack",23,98],
        ["Maarry",22,87],
        ["Lili",18,76],
    ]
    writer.writerows(lst)