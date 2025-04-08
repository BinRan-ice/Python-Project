# coding:utf-8

#创建或打开文件
file=open("文件/test.txt","w",encoding="utf-8")
#写入一条信息
file.write("hello world")
#关闭文件
file.close()