# coding:utf-8
import threading
import time

class CodingThread1(threading.Thread):
    def run(self) -> None:
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

if __name__ == '__main__':
    mult()