# coding:utf-8
import mysql.connector

# 创建连接对象
conn = mysql.connector.connect(host="192.168.154.128", user="root", passwd="root123456", database="python数据库",
                               port=3309)
# print(conn)
mycursor = conn.cursor()
# 编写sql语句
sql = "insert into student (id,name,sex,score) values (%s,%s,%s,%s)"
val = (1, "张三", "男", 98)
# 执行sql语句
mycursor.execute(sql, val)
# 提交
conn.commit()
print(mycursor.rowcount, "记录插入成功")
