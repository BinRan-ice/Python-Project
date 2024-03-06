# coding:utf-8
import mysql.connector

# 创建连接对象
conn = mysql.connector.connect(host="192.168.154.128", user="root", passwd="root123456", database="python数据库",
                               port=3309)
# print(conn)
mycursor = conn.cursor()
# 编写sql语句
#sql = "update student set score=70 where name ='张三'"
sql="delete from student where name='王五'"
# 执行sql语句
mycursor.execute(sql)
conn.commit()
print(mycursor.rowcount, "删除成功")
