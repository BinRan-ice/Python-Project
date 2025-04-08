# coding:utf-8
import numpy as np

#对数组做加法运算
n1=np.array([1,2,3])
n2=np.array([4,5,6])
print("n1+n2=",n1+n2)   #对数组做加法运算

#减法和乘除法运算
print("n1-n2=",n1-n2)   #对数组做减法运算
print("n1*n2=",n1*n2)   #对数组做乘法运算
print("n1/n2=",n1/n2)   #对数组做除法运算

#两个数组做幂运算
print("n1**n2=",n1**n2) #对数组做幂运算

#使用逻辑运算符比较数组
print("n1<2",n1<2)  #使用逻辑运算符比较数组
print("n1>2",n1>2)  #使用逻辑运算符比较数组
print("n1==2",n1==2)    #使用逻辑运算符比较数组
print("n1!=2",n1!=2)    #使用逻辑运算符比较数组
print("n1>=2",n1>=2)    #使用逻辑运算符比较数组
print("n1<=2",n1<=2)    #使用逻辑运算符比较数组

#复制数据，比较复制的结果与原数组是否相同
n3=n1.copy()
print(n1==n3)
n3[0]=9
print(n1)
print(n3)
print(n1==n3)
