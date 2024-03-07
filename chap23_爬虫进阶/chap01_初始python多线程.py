# coding:utf-8
import time
import threading

def fun1():
    for i in range(5):
        print(f"fun1中i的值为{i}")
        time.sleep(1)

def fun2():
    for i in range(5):
        print(f"fun2中i的值为{i}")
        time.sleep(1)

def single():
    fun1()
    fun2()

def mult():
    t1=threading.Thread(target=fun1)    #不能写fun(),如果这么写，是将fun1函数的结果给target
    t2=threading.Thread(target=fun2)
    #启动线程
    t1.start()
    t2.start()

if __name__ == '__main__':
    mult()