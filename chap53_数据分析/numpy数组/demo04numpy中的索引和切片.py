# coding:utf-8
import numpy as np

us_file_path = "../文件/US_video_data_numbers.csv"
uk_file_path = "../文件/GB_video_data_numbers.csv"

# delimiter:以什么分割数据,dtype:数据类型,unpack:对数据进行转置
t1 = np.loadtxt(us_file_path, delimiter=",", dtype='int', unpack=False)

# 取一行数据
# print(t1[2])
# print(t1[2,:])

# 取连续多行数据
# print(t1[2:8])
# print(t1[2:8,:])

# 取不连续的多行
# print(t1[[2, 8, 10]])
# print(t1[[2, 8, 10], :])

# 取一列数据
# print(t1[:, 0])

# 取连续的多列数据
# print(t1[:, 1:])

# 取不连续的多列
# print(t1[:, [0, 2]])

# 取行和列，取第三行，第一列的值
# print(t1[3,1])

# 取多行多列，取第三行到第五行，第一列到第三列
# print(t1[3:5, 1:3])

#取多个不相邻的点(0,0)(2,1)
print(t1[[0,2],[0,1]])