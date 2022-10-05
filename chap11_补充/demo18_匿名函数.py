# coding:utf-8
"""
匿名函数又被称为lamada表达式
语法：lamada 参数：返回值
fn=lamada n: n**2
print(fn)
ret=fn(10)
print(ret)
"""

#计算a+b的结果
fn =lambda a,b:a+b
print(fn(10,20))

fn=lambda a,b:(a+b,a-b)
print(fn(10,20))