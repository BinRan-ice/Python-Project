# coding:utf-8
import pymysql  # 导入 pymysql

userName = ""  # 记录用户名


# 打开数据库连接
def open():
    db = pymysql.connect(host="192.168.154.128", user="root", passwd="root123456", database="PyQt5实战项目",
                         port=3309)
    return db  # 返回数据库连接对象


# 执行数据库的增删改操作
def exec(sql, values):
    db = open()  # 打开数据库连接
    cursor = db.cursor()  # 创建游标对象
    try:
        cursor.execute(sql, values)  # 执行sql语句
        db.commit()  # 提交事务
        return 1  # 返回1表示执行成功
    except:
        db.rollback()  # 发生错误时回滚事务
        return 0  # 返回0表示执行失败
    finally:
        cursor.close()  # 关闭游标
        db.close()  # 关闭数据库连接


# 带参数的精确查询
def query(sql, *keys):
    db = open()  # 打开数据库连接
    cursor = db.cursor()  # 创建游标对象
    cursor.execute(sql, keys)  # 执行sql语句
    result = cursor.fetchall()  # 获取查询结果
    cursor.close()  # 关闭游标
    db.close()  # 关闭数据库连接
    return result  # 返回查询结果


# 不带参数的模糊查询
def query2(sql):
    db = open()  # 打开数据库连接
    cursor = db.cursor()  # 创建游标对象
    cursor.execute(sql)  # 执行sql语句
    result = cursor.fetchall()  # 获取查询结果
    cursor.close()  # 关闭游标
    db.close()  # 关闭数据库连接
    return result  # 返回查询结果
