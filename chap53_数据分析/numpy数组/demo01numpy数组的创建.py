# coding:utf-8
import numpy as np
import random

# 使用numpy创建数组，得到ndarray数据类型
t1 = np.array([1, 2, 3])
print(t1)

t2 = np.array(range(10))
print(t2)

t3 = np.arange(4, 12, 2)
print(t3)

# 查看数据类型
print(t3.dtype)

# 创建数组的时候指定类型
t4 = np.array(range(1, 4), dtype=float)
print(t4, t4.dtype)

t5 = np.array([1, 0, 1, 1, 0, 1, 0], dtype=bool)
print(t5, t5.dtype)

# 在已有数据类型的基础上改变数据类型
t6 = t5.astype("int8")
print(t6, t6.dtype)

# numpy中的小数
t7 = np.array([random.random() for i in range(10)])
print(t7)

# 对小数进行操作
t8 = np.round(t7, 2)  # 保留两位小数
print(t8)