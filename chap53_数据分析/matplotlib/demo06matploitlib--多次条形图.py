# coding:utf-8
from matplotlib import pyplot as plt
import matplotlib

# 设置字体
font = {'family': 'MicroSoft YaHei',
        'size': 11
        }
matplotlib.rc("font", **font)

# 数据
a = ["猩球崛起3：终极之战", "敦刻尔克", "蜘蛛侠：英雄归来", "战狼2"]
b_16 = [15746, 312, 4497, 319]
b_15 = [12357, 156, 2045, 168]
b_14 = [2358, 399, 2358, 362]
x_14 = list(range(len(a)))
x_15 = [i + 0.2 for i in x_14]
x_16 = [i + 0.4 for i in x_14]

# 调整画布
plt.figure(figsize=(16, 8), dpi=80)

# 画图描点
plt.bar(range(len(a)), b_14, width=0.2, label="14日")
plt.bar(x_15, b_15, width=0.2, label="15日")
plt.bar(x_16, b_16, width=0.2, label="16日")

# 调整坐标
plt.xticks(x_15, a)

# 添加描述信息
plt.xlabel("电影名字")
plt.ylabel("票房")
plt.title("不同日期各大电影票房")

# 添加图例
plt.legend()

plt.show()
