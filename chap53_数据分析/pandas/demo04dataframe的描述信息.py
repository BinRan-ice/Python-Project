# coding:utf-8
import pandas as pd
import pymongo

#连接到服务器
client=pymongo.MongoClient('192.168.154.128',27017,username="root",password="root123456")

#获取要操作的数据库
db=client.lianjia

#获取要操作的集合
collection=db.collection_lianjia

#查询全部数据
result=list(collection.find())
data_list=[]
for i in result:
    temp={}
    temp["title"]=i["title"]
    temp["number"]=i["number"]
    temp["unitPrice"]=i["unitPrice"]
    data_list.append(temp)

#使用DataFrame读取数据
datas=pd.DataFrame(data_list)
print(datas)

# #DataFrame的基础属性
#
# #显示行数和列数
# print(datas.shape)
# #显示行索引
# print(datas.index)
# #显示列索引
# print(datas.columns)
# #对象的值
# print(datas.values)
# #列数据类型
# print(datas.dtypes)
# #数据的维度
# print(datas.ndim)
#
# #DataFrame整体情况查询
#
# #显示头部几行，默认五行
# print(datas.head(4))
# #显示尾部几行，默认五行
# print(datas.tail(4))
# #相关信息概览：行数，列数，列索引，列非空值个数，列类型，内存占用
# print(datas.info())
# #快速综合统计结果：计数，均值，标准差，最大值，四分位数，最小值
# print(datas.describe())

#DataFrame中的排序方法
df=datas.sort_values(by="number",ascending=False)
print(df)
