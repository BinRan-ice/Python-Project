# coding:utf-8
import threading
import time
import warnings
warnings.filterwarnings("ignore")

#定义全局变量
ticket=100

#卖票
def sale_ticket():
    global ticket   #使用全区变量
    for i in range(1000):
        if ticket>0:
            print(threading.current_thread().getName()+f'-->正在出售第{ticket}张票')
            ticket-=1
        time.sleep(1)

#k开辟两个线程
def start():
    for i in range(2):
        t=threading.Thread(target=sale_ticket)
        t.start()

if __name__ == '__main__':
    start() #启动线程