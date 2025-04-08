# coding:utf-8
import numpy as np

n1=np.array([1,2,3])    #创建一维数组
n2=np.array([0.1,0.2,0.3])  #创建一维小数数组
n3=np.array([[1,2,3],[4,5,6]]) #创建二维数组

#创建浮点型数组
list=[1,2,3]
n4=np.array(list,dtype=float)
print(n4)
print(n4.dtype)
print(type(n4[0]))

#创建三维数组
nd1=[1,2,3]
nd2=np.array(nd1,ndmin=3)   #ndmin=3表示创建三维数组
print(nd2)

#创建两行三列的未初始化的数组
n5=np.empty([2,3])
print(n5)

#创建用0填充的数组
n6=np.zeros((3,3),np.uint8)
print(n6)

#创建用1填充的数组
n7=np.ones((3,3),np.uint8)
print(n7)

#创建随机数组
n8=np.random.randint(1,3,10)
print("随机生成10个1到3且不包括3的整数：",n8)
n9=np.random.randint(5,10)
print("size数组大小为空随机返回一个整数：",n9)
n10=np.random.randint(5,size=(2,5))
print("随机生成5以内的二维数组：",n10)

