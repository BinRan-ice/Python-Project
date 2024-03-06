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

#修改操作--一次修改一条数据
#collection.update_one({'name':'李四'},{'$set':{'age':20}})

#修改操作--一次修改多条数据
#collection.update_many({'name':'王五'},{'$set':{'gender':'男'}})

#删除操作--一次删除一条数据
#collection.delete_one({'name':'李四'})

#删除操作--一次删除多条数据
collection.delete_many({'age':20})