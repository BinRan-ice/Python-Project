# coding:utf-8
import numpy as np

#查找一维数组索引为0的元素
n1=np.array([1,2,3]) #创建一维数组
print(n1[0]) #查找一维数组索引为0的元素

#获取数组中某范围内的元素
print(n1[0])
print(n1[1])
print(n1[0:2])
print(n1[1:])
print(n1[:2])

#使用不同的切片式索引操作获取数组中的元素
n2=np.array([0,1,2,3,4,5,6,7,8,9])
print(n2)
print(n2[:3])
print(n2[3:6])
print(n2[6:])
print(n2[::])
print(n2[:])
print(n2[::2])
print(n2[1::5])
print(n2[2::6])
#start:stop:step为切片式索引操作的格式，start表示开始索引，stop表示结束索引，step表示步长，当为负数时表示从右向左取值
print(n2[::-1])
print(n2[:-3:-1])
print(n2[-3:-5:-1])
print(n2[-5::-1])

#用三种方式获取二维数组中的元素
#创建三行四列的二维数组
n3=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(n3[1])
print(n3[1][2])
print(n3[-1])

#使用切片式索引操作获取二维数组中的元素
#创建三行三列的二维数组
n4=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(n4[:2,1:])
print(n4[1,:2])
print(n4[:2,2])
print(n4[:,:1])