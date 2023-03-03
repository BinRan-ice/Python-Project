# coding:utf-8

# lst = [13, 28, 1, 36, 17, 58]
#
# res = sorted(lst, reverse=True)
# print(res)

# lst = ["赵本山", "斯琴高娃", "周杰", "丁俊晖"]
#
# # 需要自己去定义排序规则
# # 根据名字的长度进行排序
# # def func(item):
# #     return len(item)
#
#
# res = sorted(lst, key=lambda item: len(item))
# print(res)

#
# lst = [{"id": 1, "name": '盖伦', "age": 18},
#        {"id": 2, "name": '杰斯', "age": 16},
#        {"id": 3, "name": '压缩', "age": 17}]
# # 按照年龄对学生信息进行排序
# print(sorted(lst, key=lambda dic: dic['age']))


# lst = [7, 21, 3, 46, 61, 3, 5]
# # 请把能被3整除的数摘出来
# f = filter(lambda x: x % 3 == 0, lst)
# print("__iter__" in dir(f))
# print(list(f))


# lst = [{"id":1, "name":'jolin', "age":18},
#        {"id":2, "name":'tony', "age":16},
#        {"id":3, "name":'kevin', "age":17}]
#
# # 把年龄大于等于17岁的人拿到
# f = filter(lambda x: x['age'] >= 17 , lst)
# print(list(f))


# lst = [18, 22, 17, 5, 9]
# # 让列表中的每一个数字都增加1
# m = map(lambda x: x + 1, lst)
# print(list(m))
#
# lst2 = [item+1 for item in lst]
# print(lst2)

"""
callable()
dir()
open()
bin()
oct()
hex()
chr()
ord()
format()
zip() 拉链
any()
all()
sorted()
filter()
map()
"""