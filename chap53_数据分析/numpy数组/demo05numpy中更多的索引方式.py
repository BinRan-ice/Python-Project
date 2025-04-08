# coding:utf-8
import numpy as np

t2 = np.arange(24).reshape((4, 6))

# 查询t2中小于10的元素,赋值为3
# t2[t2 < 10] = 3

# 把t2中小于10的替换为0，大于10的替换为10
# print(np.where(t2<10,0,10))

#把t2中小于15的替换成15大于20的替换成20
print(t2.clip(15,20))

#t=替换元素为nan
t2=t2.astype(float)
t2[3,3]=np.nan
print(t2)