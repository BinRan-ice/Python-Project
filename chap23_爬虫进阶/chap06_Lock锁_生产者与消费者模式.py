# coding:utf-8
import threading
import random
import time
import warnings
warnings.filterwarnings("ignore")

#共享资源
g_money=0

#创建锁对象
lock=threading.Lock()

#生产者
class Producer(threading.Thread):
    def run(self) -> None:
        global g_money
        for _ in range(10):
            lock.acquire()
            money=random.randint(1000,10000)
            g_money+=money
            print(threading.current_thread().getName()+f'挣了{money}钱,当前的余额为{g_money}')
            time.sleep(1)
            lock.release()

#消费者
class Customer(threading.Thread):
    def run(self) -> None:
        global g_money
        for _ in range(10):
            lock.acquire()
            money=random.randint(100,10000)
            if money<=g_money:
                g_money-=money
                print(threading.current_thread().getName()+f'花了{money}钱,当前余额为{g_money}')
            else:
                print(threading.current_thread().getName()+f'想花{money}钱,但是余额不足，当前余额为：{g_money}')
            time.sleep(1)
            lock.release()

def start():
    for i in range(5):
        th=Producer(name=f"生产者{i}")
        th.start()
    for j in range(5):
        cust=Customer(name=f'消费者{j}')
        cust.start()

if __name__ == '__main__':
    start()