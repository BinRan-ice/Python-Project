# coding:utf-8
import numpy as np

# 两个nan是不相等的
# print(np.nan == np.nan)

# 判断数组中不为的个数
# t2 = np.arange(24).reshape((4, 6))
# t2[:,0]=0
# print(np.count_nonzero(t2))

# 判断t2!=t2
# t2 = np.arange(24).reshape((4, 6))
# t2=t2.astype(float)
# t2[3,3]=np.nan
# print(t2!=t2)
# 判断nan值的个数
# print(np.count_nonzero(t2!=t2))

# 判断当前值是否是nan
# print(np.isnan(t2))

# nan和任何值计算都是nan
# print(np.sum(t2))
# t3=np.arange(24).reshape((4, 6))
# print(np.sum(t3,axis=0))
# print(np.sum(t3,axis=1))
# print(np.sum(t2,axis=0))

# 常用统计方法
t2 = np.arange(24).reshape((4, 6))
t2=t2.astype(float)
t2[3,3]=np.nan
print(t2.sum(axis=0))
print(t2.mean(axis=0))          #计算均值
print(np.median(t2,axis=0))     #计算均值
print(t2.max(axis=0))           #最大值
print(t2.min(axis=0))           #最小值
print(np.ptp(t2,axis=0))        #计算极值：最大值最小值上的差
print(t2.std)                   #标准差