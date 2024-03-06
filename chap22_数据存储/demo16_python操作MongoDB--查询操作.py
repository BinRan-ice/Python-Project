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

#查询全部数据
# result=collection.find()
# for item in result:
#     print(item)

#查询姓名是王五的学生
# result=collection.find({'name':'王五'})
# for item in result:
#     print(item)

#查询姓名当中包含二的学生
# result=collection.find({'name':{'$regex':'.*二.*'}})
# for item in result:
#     print(item)

#将查询结果排序
# result=collection.find().sort('age',pymongo.ASCENDING)
# for item in result:
#     print(item)

#将查询结果分页
# result=collection.find().sort('age',pymongo.DESCENDING).limit(3)
# for item in result:
#     print(item)

#显示4,5,6条数据
result=collection.find().sort('age',pymongo.DESCENDING).skip(3).limit(3)
for item in result:
    print(item)