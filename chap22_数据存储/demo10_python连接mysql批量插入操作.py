# coding:utf-8
import mysql.connector

# 创建连接对象
conn = mysql.connector.connect(host="192.168.154.128", user="root", passwd="root123456", database="python数据库",
                               port=3309)
# print(conn)
mycursor = conn.cursor()
# 编写sql语句
sql = "insert into student (id,name,sex,score) values (%s,%s,%s,%s)"
vals = [
    (2, "李四", "男", 72),
    (3, "王五", "男", 91),
    (4, "赵六", "男", 51)
]
mycursor.executemany(sql, vals)
conn.commit()
print(mycursor.rowcount, "插入记录成功")
