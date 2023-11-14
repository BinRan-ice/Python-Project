# coding:utf-8
import pandas as pd #做数据处理和分析，清洗
import matplotlib.pyplot as plt #用来做可视化的工具，能把数据变成图表

#引入数据
df = pd.read_csv('data/data.csv',header=None,index_col=0)#处理表头和行索引

#把红球的号码拿出来
#列：从1拿到6
#行：所有行的数据都是想要的数据
red_ball=df.loc[:,1:6]
#print(red_ball)
#把蓝球的号码拿出来
blue_ball=df.loc[:,7]
#print(blue_ball)

#做数据统计
#每个号码出现的次数
red_ball_count=pd.value_counts(red_ball.values.flatten())
#print(red_ball_count)
blue_ball_count=pd.value_counts(blue_ball)
#print(blue_ball_count)

#可视化展示->制作成图表
#fig,ax=plt.subplots(2,1)  #一次创建很多个图表
#用饼状图来展示
plt.pie(red_ball_count,labels=red_ball_count.index,radius=1,wedgeprops={"width":0.3})
plt.pie(blue_ball_count,labels=blue_ball_count.index,radius=0.5,wedgeprops={"width":0.2})
plt.show()  #展示图表