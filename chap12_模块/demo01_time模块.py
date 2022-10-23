# coding:utf-8
import time
#sleep()    可以暂停执行一段时间
print("你好")
time.sleep(3)
print("你才好呢")

print(time.time())      #1664521592-->时间戳   数字类型的时间

#可以计算时间差
start=time.time()
for i in range(10000):
    print(i)
end=time.time()
print(end-start)