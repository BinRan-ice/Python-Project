# coding:utf-8
from redis import Redis
from pymongo import MongoClient
import json
"""
将redis中的数据转移到MongoDB中
"""

# 创建redis连接
redis_client = Redis(host='192.168.154.128', port=6379, password="redis123456", username="default")
# 创建MongoDB的连接
mongo_client = MongoClient('192.168.154.128', 27017, username="root", password="root123456")
while True:
    # 从redis取数据
    source, data = redis_client.blpop(['lianjia:items'])
    change_data = json.loads(data)  # dict
    lianjia = mongo_client.zufang.lianjia2
    lianjia.insert_one(change_data)
