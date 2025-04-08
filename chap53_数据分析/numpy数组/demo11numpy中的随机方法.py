# coding:utf-8
import numpy as np

# 打印方阵
print(np.eye(4))

# 获取最大值最小值的位置
t = np.arange(24).reshape((4, 6))
print(t)
print(np.argmax(t, axis=0))
print(np.argmin(t, axis=1))

# numpy生成随机数
# 创建一个四行五列的10-20的整数数组
print(np.random.randint(10, 20, (4, 5)))
# 创建一个两行三列均匀分布的数组
print(np.random.rand(2, 3))
# 创建一个两行三列标准正态分布的数组
print(np.random.randn(2, 3))
# 创建一个四行五列的10-20的小数数组
print(np.random.uniform(10,20,(4,5)))
#创建一个随机种子,指定随机种子后生成的数组是一样的
np.random.seed(10)
print(np.random.randint(10, 20, (4, 5)))