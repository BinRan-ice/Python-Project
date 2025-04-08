# coding:utf-8
from matplotlib import pyplot as plt
import random
import matplotlib
# from matplotlib import font_manager

# 设置字体
# my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/simkai.ttf")
font = {'family': 'MicroSoft YaHei',
        'size': 11
        }
matplotlib.rc("font", **font)

# x轴，y轴数据
x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]

# 设置图片大小
plt.figure(figsize=(16, 8), dpi=80)

# 描点画图
plt.plot(x, y)

# 调整x轴刻度
_x = list(x)
_xtick_labels = [f"10点{i}分" for i in range(60)]
_xtick_labels += [f"11点{j}分" for j in range(60)]

# 取步长，数字和字符串一一对应，数据的长度一样
plt.xticks(_x[::10], _xtick_labels[::10], rotation=90)  # rotation旋转的度数
# plt.xticks(_x[::10], _xtick_labels[::10], rotation=90, fontproperties=my_font) fontproperties设置字体
# plt.xticks(_x[::10], _xtick_labels[::10], rotation=90, fontproperties="STSong") fontproperties设置字体

#添加描述信息
plt.xlabel("时间")
plt.ylabel("温度(单位:℃)")
plt.title("10点到12点每分钟的气温变化情况")

plt.show()
