# coding:utf-8

# a = 10
# def func():
#     a = 20
#     print(locals())
#
# func()
# print(globals())  # 查看全局作用域所有内容
# print(locals())  # 查看当前作用域中的内容


# for i in range(10):
#     print(i)


# lst = [11,22,33]
# it = lst.__iter__()
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# it = iter(lst)
# print(next(it))
# print(next(it))
# print(next(it))

# def iter(obj):
#     return obj.__iter__()
# def next(obj):
#     return obj.__next__()

# print(dir(bool))


# # callable(xxx) 判断xxx是否是可以被调用的, 是否可以在后面添加括号
# def func():
#     pass
#
#
# print(callable(func))
# print(callable(123))



# def run():
#     print("我会跑")
#
#
# def jump():
#     print("我也会跳")
#
#
# def func(fn):
#     if callable(fn):  # 判断该内容是否可以被调用
#         fn()
#     else:
#         print("您输入的内容不可以被直接调用")
#
# func(run)
# func(jump)
# func(123)


# print(help(str))


# import copy
# import os
#
# # mo = input(">>>")  # "os"
# # __import__(mo)   # 动态加载一个模块


# f = open("xxx", mode="", encoding="utf-8")
# f.read()
# for line in f:
#     pass
#
# f.write()
#
# with open() as f:
#     pass


# lst = [111,222,333]
# lst2 = [111,222,333]
# print(id(lst), id(lst2))

# print(hash("呵呵"), hash("呵呵"))


# s = "1+1"
# r = eval(s)  # 可以把字符串当成代码去执行, 有返回值
# print(r)


# s = "a = 100"
# exec(s)  # 没有返回值
# print(a)  # pycharm报错, 不一定是错.


# # compile() 把一段字符串代码加载. 后面可以通过exec和eval去执行
# c1 = compile("for i in range(10):print(i)", "", "exec")
# exec(c1)


# c2 = compile("1+2+3", "", "eval")
# r = eval(c2)
# print(r)

# c3 = compile("n = int(input('>>>:'))", "", "single")
# exec(c3)
# print(n)


# # eval: 可以把字符串当代码执行, 有返回值
# s = "['张无忌', '张翠山', '张三丰']"
# lst = eval(s)
# print(lst, type(lst))

# # 问题: 安全性问题
# s = input("请输入你要执行的代码:")
# exec(s)
# print("hello world")
