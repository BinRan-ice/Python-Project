# coding:utf-8
import numpy as np
from matplotlib import pyplot as plt

us_file_path = "../文件/US_video_data_numbers.csv"
uk_file_path = "../文件/GB_video_data_numbers.csv"

#delimiter:以什么分割数据,dtype:数据类型,unpack:对数据进行转置
t_us = np.loadtxt(uk_file_path,delimiter=",",dtype='int')

#取评论的数据
t_us_comments=t_us[:,-1]
#选择比500小的数据
t_us_comments=t_us_comments[t_us_comments<=5000]
d=250
bin_nums=(t_us_comments.max()-t_us_comments.min())//d

#绘图
plt.figure(figsize=(16,8),dpi=80)
plt.hist(t_us_comments,bin_nums)
plt.show()