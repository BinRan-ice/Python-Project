# coding:utf-8
from matplotlib import pyplot as plt
import matplotlib

# 设置字体
font = {'family': 'MicroSoft YaHei',
        'size': 11
        }
matplotlib.rc("font", **font)

# 3月份10月份数据
y_3 = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14, 17, 18, 21, 16, 17, 20, 14, 15, 15, 15, 19, 21, 22, 22,
       22,
       23]
y_10 = [26, 26, 28, 19, 21, 17, 16, 19, 18, 20, 20, 19, 22, 23, 17, 20, 21, 20, 22, 15, 11, 15, 5, 13, 17, 10, 11, 13,
        12,
        13, 6]
x_3 = range(1, 32)
x_10 = range(51, 82)
# 设置画布大小
plt.figure(figsize=(16, 8), dpi=80)

# 描点绘图
plt.scatter(x_3, y_3, label="3月份", color="yellow")
plt.scatter(x_10, y_10, label="10月份", color="cyan")

# 调整x,y轴坐标
_x = list(x_3) + list(x_10)
_xtick_labels = [f"3月{i}日" for i in x_3]
_xtick_labels += [f"10月{j - 50}日" for j in x_10]
plt.xticks(_x[::3], _xtick_labels[::3], rotation=45)

# 设置描述信息
plt.xlabel("月份")
plt.ylabel("气温(℃)")
plt.title("3月份与10月份每天温度示意图")

# 添加图例
plt.legend()

plt.show()
