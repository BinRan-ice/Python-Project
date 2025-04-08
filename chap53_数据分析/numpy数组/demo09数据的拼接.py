# coding:utf-8
import numpy as np

t1=np.arange(12).reshape(2,6)
t2=np.arange(12,24).reshape(2,6)

#竖直拼接
print(np.vstack((t1,t2)))

#水平拼接
print(np.hstack((t1,t2)))

#行交换
t=np.arange(12,24).reshape(3,4)
t[[1,2],:]=t[[2,1],:]
print(t)

#列交换
t3=np.arange(12,24).reshape(3,4)
t3[:,[0,2]]=t3[:,[2,0]]
print(t3)