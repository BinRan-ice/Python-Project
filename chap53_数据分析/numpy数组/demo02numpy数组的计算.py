# coding:utf-8
import numpy as np

#打印数组的行数列数
t1=np.arange(12)
print(t1.shape)

t2=np.array([[1,2,3],[4,5,6]])
print(t2.shape)

t3=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(t3.shape)

#重构矩阵的行数列数
t4=np.arange(12)
print(t4)
print(t4.reshape((3,4)))

t5=np.arange(24)
print(t5.reshape(2,3,4))    #变成三维数组
print(t5.reshape((4,6)))    #变成二维数组
print(t5.reshape((24,)))    #变成一维数组
t5=t5.reshape((4,6))
t6=t5.reshape(t5.shape[0]*t5.shape[1],)
print(t6)

#将多维数组展开为一维数组
print(t5.flatten())

#数组的计算
print(t5+2)
print(t5*2)
t7=np.arange(100,124).reshape((4,6))
print(t5+t7)
t8=np.arange(0,6)
print(t5-t8)
t9=np.arange(4).reshape((4,1))
print(t5-t9)

t10=np.arange(18).reshape((3,3,2))
t11=np.arange(3).reshape((3,1))
print(t11)
print(t10)
print(t10+t11)
