# coding:utf-8
import mysql.connector

# 创建连接对象
conn = mysql.connector.connect(host="192.168.154.128", user="root", passwd="root123456", database="python数据库",
                               port=3309)
# print(conn)
mycursor = conn.cursor()
# 编写sql语句
sql = "select * from student"
# 执行查询操作
mycursor.execute(sql)
# 获取所有查询记录
myresult = mycursor.fetchall()
for item in myresult:
    print(item)
