# coding:utf-8
import numpy as np

us_file_path = "../文件/US_video_data_numbers.csv"
uk_file_path = "../文件/GB_video_data_numbers.csv"

#delimiter:以什么分割数据,dtype:数据类型,unpack:对数据进行转置
t1 = np.loadtxt(us_file_path,delimiter=",",dtype='int',unpack=True)
print(t1)

#转置
t2=np.arange(24).reshape((4,6))
print(t2.transpose())
print(t2.T)
print(t2.swapaxes(1,0)) #交换0轴，1轴