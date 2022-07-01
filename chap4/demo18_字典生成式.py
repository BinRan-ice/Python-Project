# coding:utf-8
import random
d={item:random.randint(1,100) for item in range(4)}
print(d)

#创建两个列表
lst=[1001,1002,1003]
lst2=['陈美美','王一一','李丽丽']
d={key:value for key,value in zip(lst,lst2)}
print(d)