# coding:utf-8
from matplotlib import pyplot as plt
import matplotlib

# 设置字体
font = {'family': 'MicroSoft YaHei',
        'size': 11
        }
matplotlib.rc("font", **font)

# 数据
a = ["战狼2", "速度与激情8", "功夫瑜伽", "西游伏妖篇", "变形金刚5:最后的骑士", "摔跤吧!爸爸", "加勒比海盗5:死无对证", "金刚:骷髅岛", "极限特工:终极回归", "生化危机6:终章",
     "乘风破浪", "神偷奶爸3", "智取威虎山", "大闹天竺", "金刚狼3:殊死一战", "蜘蛛侠英雄归来", "悟空传", "银河护卫队2", "情圣", "新木乃伊"]
b = [56.01, 26.94, 17.53, 16.49, 15.45, 12.96, 11.8, 11.61, 11.28, 11.12, 10.49, 10.3, 8.75, 7.55, 7.32, 6.99, 6.88,
     6.86, 6.58, 6.23]

# 设置画布大小
plt.figure(figsize=(16, 8), dpi=80)

# 描点画图--横着的条形图
plt.barh(a, b, height=0.3, color="orange")

# 调整x，y轴
plt.yticks(a)

# 添加网格
plt.grid(0.7)

# 添加描述信息
plt.ylabel("电影")
plt.xlabel("票房(:亿)")
plt.title("电影票房示意图")

plt.show()
