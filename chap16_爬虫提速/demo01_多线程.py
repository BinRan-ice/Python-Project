# coding:utf-8
from threading import Thread

"""
进程:资源单位，每一个进程至少有一个线程
线程：执行单位
"""

"""
单线程：
def func():
    for i in range(1000):
        print("func",i)

#启动每一个程序默认会有一个主线程
if __name__ == '__main__':
    func()
    for i in range(1000):
        print("main",i)
"""


# #多线程
# def func():
#     for i in range(1000):
#         print("func",i)
#
# if __name__ == '__main__':
#     t=Thread(target=func)
#     t.start()   #多线程状态为可以开始工作状态，具体的执行时间由CPU决定
#     for i in range(1000):
#         print("main",i)

class MyThread(Thread):
    def run(self):  # 固定的   当线程被执行的时候，被执行的就是run
        for i in range(1000):
            print("子线程", i)


if __name__ == '__main__':
    t=MyThread()
    #t.run()     方法的调用，单线程
    t.start()   #开启线程
    for i in range(1000):
         print("main",i)

"""
def func(name):
    for i in range(1000):
        print("name",i)

if __name__ == '__main__':
    t1=Thread(target=func,args=("周杰伦",))        #传递参数必须是元组
    t1.start()
    t2=Thread(target=func,args=("王力宏",))
    t2.start()       
"""