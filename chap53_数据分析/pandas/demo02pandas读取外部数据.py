# coding:utf-8
import pandas as pd
import pymongo

#使用pandas读取csv文件
df = pd.read_csv("../文件/豆瓣.csv")
print(df)

#使用pandas读取mongdb中的数据

#连接到服务器
client=pymongo.MongoClient('192.168.154.128',27017,username="root",password="root123456")

#获取要操作的数据库
db=client.lianjia

#获取要操作的集合
collection=db.collection_lianjia

#查询全部数据
result=list(collection.find())

#使用Series读取数据
data=result[0]
data=pd.Series(data)
print(data)

#使用DataFrame读取数据
datas=pd.DataFrame(result)
print(datas)