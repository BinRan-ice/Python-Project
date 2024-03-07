# coding:utf-8
from queue import Queue

#FIFO
#创建一个队列，最多存放5个数据
q=Queue(5)
#向队列中存放数据
for i in range(4):
    q.put(i)
print("队列中实际数据得多少：",q.qsize())
#取出数据
for _ in range(5):
    try:
        print(q.get(block=False))
    except:
        print("数据已经取完，队列目前为空")
        break

if q.full():
    print("队列已满")
else:
    print("队列当前数据的个数为：",q.qsize(),"队列不满")

print("*"*50)
q2=Queue(5)
for i in range(6):
    try:
        q2.put(i,block=False)
    except:
        print("队列已满")
        break
print("程序结束")