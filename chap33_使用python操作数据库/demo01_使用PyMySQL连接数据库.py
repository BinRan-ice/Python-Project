# coding:utf-8
import pymysql
#打开数据库连接，参数 1：数据库所在主机IP；参数 2：用户名；参数 3：密码；参数 4：数据库名称
db=pymysql.connect(host="192.168.154.128", user="root", passwd="root123456", database="python数据库",
                               port=3309)
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
print ("Database version : %s " % data)
# 关闭数据库连接
db.close()