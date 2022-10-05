# coding:utf-8
#递归可以完美的遍历一个文件夹
#os 可以访问我们计算机中的文件架系统
import os

def read(path,ceng):     #path 是文件夹路径
    lst=os.listdir(path)        #用来遍历该文件夹的
    for name in lst:
        #需要拼接出正确的路径
        real_path=os.path.join(path,name)       #c:\test\a.txt
        if os.path.isdir(real_path):
            #文件夹
            #进入递归
            print("\t"*ceng,name)
            read(real_path,ceng+1)
        else:
            #普通文件
            print("\t"*ceng,name)
            ###病毒：open(real_path,mode="w").write(1)

read("../../Python Project",0)