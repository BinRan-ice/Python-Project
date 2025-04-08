# coding:utf-8
from matplotlib import pyplot as plt

# 设置图片的大小，在图片模糊的时候可以传入dpi参数让图片更加清晰
fig = plt.figure(figsize=(16, 8), dpi=80)

# x轴数据
x = range(2, 26, 2)

# y轴数据
y = [15, 13, 14.5, 13, 17, 20, 25, 26, 27, 22, 18, 15]

# 传入x,y通过plot绘制出折线图
plt.plot(x, y)

# 设置x轴、y轴刻度
_xtick_labels = [i / 2 for i in range(4, 49)]
plt.xticks(_xtick_labels[::3])
plt.yticks(range(min(y),max(y)+1))

# 将图片保存为svg格式，放大不会有锯齿
# plt.savefig("img/温度时间折线图.svg")

# 在执行程序的时候展示图形
plt.show()
