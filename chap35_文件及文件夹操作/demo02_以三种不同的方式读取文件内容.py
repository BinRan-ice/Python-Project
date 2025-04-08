# coding:utf-8

with open("文件/test.txt", "r", encoding="utf-8") as file:
    #读取前5个字符
    print(file.read(5))
    #读取第一行数据
    print(file.readline())
    #读取所有行数据
    print(file.readlines())