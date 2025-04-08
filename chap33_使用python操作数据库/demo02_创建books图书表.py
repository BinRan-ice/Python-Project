# coding:utf-8
import pymysql
#打开数据库连接
db=pymysql.connect(host="192.168.154.128", user="root", passwd="root123456", database="python数据库",
                               port=3309)
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 如果数据表已经存在使用 execute() 方法删除表。
cursor.execute("DROP TABLE IF EXISTS books")
# 创建数据表SQL语句
sql="""
CREATE TABLE books(
    id int(8) NOT NULL AUTO_INCREMENT,
    name varchar(50) NOT NULL,
    category varchar(50) NOT NULL,
    price decimal(10,2) DEFAULT NULL,
    publish_time date DEFAULT NULL,
    PRIMARY KEY (id)
)ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
"""
#执行SQL语句
cursor.execute(sql)
# 关闭数据库连接
db.close()