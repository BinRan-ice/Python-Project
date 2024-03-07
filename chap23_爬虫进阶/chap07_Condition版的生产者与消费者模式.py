# coding:utf-8
import threading
import random
import time
import warnings
warnings.filterwarnings("ignore")

#共享资源
g_money=0

#创建Condition对象
lock=threading.Condition()

#共享次数
g_time=0

#生产者
class Producer(threading.Thread):
    def run(self) -> None:
        global g_money
        global g_time
        for _ in range(10):
            lock.acquire()
            money=random.randint(1000,10000)
            g_money+=money
            g_time+=1
            print(threading.current_thread().getName()+f'挣了{money}钱,当前的余额为{g_money}')
            #time.sleep(1)
            lock.notify_all()
            lock.release()

#消费者
class Customer(threading.Thread):
    def run(self) -> None:
        global g_money
        for _ in range(10):
            lock.acquire()
            money=random.randint(100,10000)
            while g_money<money:
                if g_time>=50:
                    lock.release()
                    return
                print(threading.current_thread().getName()+f"想花{money}钱，但是余额不足,余额为：{g_money}")
                #余额不足的情况下需要等待
                lock.wait()
            #开始消费
            g_money-=money
            print(threading.current_thread().getName() + f"花了{money}钱，当前余额为：{g_money}")
            #time.sleep(1)
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