# coding:utf-8
import threading
import time

class CodingThread1(threading.Thread):
    def run(self) -> None:
        #获取当前的线程对象
        thread=threading.current_thread()
        print("当前的线程对象:",thread)
        #修改线程的名称
        thread.setName("我的线程")
        #获取线程的名称
        print("线程的名称：",thread.getName())
        for i in range(5):
            print(f"fun1中i的值为{i}")
            time.sleep(1)

class CodingThread2(threading.Thread):
    def run(self) -> None:
        for i in range(5):
            print(f"fun2中i的值为{i}")
            time.sleep(1)

def mult():
    t1=CodingThread1()
    t2=CodingThread2()
    t1.start()
    t2.start()
    #获取当前运行的线程信息
    print("获取当前运行的线程信息:",threading.enumerate())

if __name__ == '__main__':
    mult()