# coding:utf-8
from matplotlib import pyplot as plt
import matplotlib

# 设置字体
font = {'family': 'MicroSoft YaHei',
        'size': 11
        }
matplotlib.rc("font", **font)

# x，y轴数据
y_1 = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
y_2 = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
x = range(0, 20)

# 设置画布大小
plt.figure(figsize=(16, 8), dpi=80)

# 描点画图
plt.plot(x, y_1, label="自己", color="#FF0000", linestyle=":")
plt.plot(x, y_2, label="同桌", color="cyan", linestyle="--")

# 设置x轴刻度
_xtick_labels = [f"{i + 11}岁" for i in x]
plt.xticks(x, _xtick_labels, rotation=90)
# plt.yticks(range(0,9))

# 添加描述信息
plt.xlabel("年龄")
plt.ylabel("女朋友数量")
plt.title("11-30岁交女朋友数量走势")

# 绘制网格
plt.grid(alpha=0.4, linestyle=":")  # alpha设置透明度

# 添加图例
plt.legend(loc="upper left")

# 显示
plt.show()
