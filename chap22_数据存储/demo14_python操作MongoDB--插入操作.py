# coding:utf-8
import pymongo

#连接到服务器
client=pymongo.MongoClient('192.168.154.128',27017,username="root",password="root123456")

#获取要操作的数据库
db=client.school
#db=client["school"]

#获取要操作的集合
collection=db.student
#collection=db["student"]

#插入操作
#stu={'name':'张一一','age':20,'gender':'女'}
#collection.insert_one(stu)

#一次插入多条数据
lst=[
    {'name':'王二二','age':23,'gender':'女'},
    {'name':'张三三','age':24,'gender':'男'},
    {'name':'智思思','age':20,'gender':'女'}
]
collection.insert_many(lst)