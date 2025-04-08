# coding:utf-8
from matplotlib import pyplot as plt
import matplotlib

# 设置字体
font = {'family': 'MicroSoft YaHei',
        'size': 11
        }
matplotlib.rc("font", **font)

# 数据
interval = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 60, 90]
width = [5, 5, 5, 5, 5, 5, 5, 5, 5, 15, 30, 60]
quantity = [836, 2737, 3723, 3926, 3596, 1438, 3273, 642, 824, 613, 215, 57]

# 设置画布大小
plt.figure(figsize=(16, 8), dpi=80)

# 画图描点
plt.bar(range(12), quantity, width=1)

# 设置x轴刻度
_x = [i - 0.5 for i in range(13)]
_xtick_labels = interval + [150]
plt.xticks(_x, _xtick_labels)

# 添加描述信息
plt.xlabel("距离公司距离")
plt.ylabel("人数")
plt.title("距离公司距离的上班人数分布")

plt.grid()
plt.show()
