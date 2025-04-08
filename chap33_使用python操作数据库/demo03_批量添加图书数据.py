# coding:utf-8
import pymysql
#打开数据库连接
db=pymysql.connect(host="192.168.154.128", user="root", passwd="root123456", database="python数据库",
                               port=3309)
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
#数据列表
data=[('零基础学python', 'python', '79.80', '2018-5-20'), ('零基础学java', 'java', '69.80', '2018-6-20'),
        ('零基础学大数据', '大数据', '89.80', '2018-7-20'), ('零基础学人工智能', '人工智能', '99.80', '2018-8-20'),
        ('零基础学云计算', '云计算', '59.80', '2018-9-20')]
try:
    # 执行sql语句，批量插入数据
    cursor.executemany("insert into books(name,category,price,publish_time) values(%s,%s,%s,%s)",data)
    # 提交到数据库执行
    db.commit()
except Exception as e:
    # 如果发生错误则回滚
    print(e)
    db.rollback()
# 关闭数据库连接
db.close()
