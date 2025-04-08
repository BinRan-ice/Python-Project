# coding:utf-8
import pandas as pd
import string
import numpy as np

#Series一维，带标签的数组
t=pd.Series(np.arange(10),index=list(string.ascii_uppercase[:10]))
print(t)

#通过字典创建Series类型
temp_dict={"name":"小红","age":30,"tel":10086}
t1=pd.Series(temp_dict)
print(t1)

#使用字典推导式生成一个字典创建Series类型
a={string.ascii_uppercase[i]:i for i in range(10)}
t2=pd.Series(a)
print(t2)

#更改数据的类型
t=t.astype(float)
print(t)

#Series的切片和索引
print(t1["age"])
print(t1["tel"])
print(t1[2])

#Series取连续的多行
print(t1[:3])

#Series取不连续的多行
print(t1[[1,2]])
print(t1[["age","tel"]])

#Series中的布尔索引
print(t[t>5])

#Series取索引,值
print(t.index,t.values)
#取索引的长度
print(len(t.index))
#遍历索引
for i in t.index:
    print(i)
#索引转换成列表
lst=list(t.index)
print(lst[:2])