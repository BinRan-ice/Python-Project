# coding:utf-8

# hg = 1.25
# print(hg)
# print(type(hg))

# # 0.111111111111111
# print(10/3)  # 计算机存储小数是有误差的


# a = 5
# print(bin(a))  # 0b101
#
# b = 0b101
# print(b)
# c = 9
# print(oct(c))  # 0o11
#
#
# d = 10
# print(hex(d))  # 0xa   0-f


# a = -16
# print(abs(a))  # 绝对值

# print(divmod(10, 3))  # 除法. (商, 余数)

# a = 9.1
# print(round(a))

# print(pow(2, 10))  # 次幂
# print(2**10)

# print(sum([1,2,3,4,5,6,7,8]))

# print(max([11,521, 1466, 3]))
# print(min([11,521, 1466, 3]))


# d = dict([("赵本山", "马大帅"), ("范伟", "范德彪")])
# print(d)

# list -> tuple
# set -> frozenset
# s = frozenset((11,22,11,33))
# print(s)


# lst = ["张无忌", "张翠山", "张三丰"]
# for item in lst:
#     print(item)
# for i in range(len(lst)):
#     print(i)
#     print(lst[i])
# for i, item in enumerate(lst, 10):
#     print(i)
#     print(item)


# lst = [0, "呵呵", True]
# print(any(lst))   # or
# print(all(lst))   # and


# lst1 = ["赵本山", "苏有朋"]
# lst2 = ["马大帅", "情深深雨蒙蒙", "情深深雨蒙蒙"]
# lst3 = ['马大帅', "啊飞", "小男孩"]
#
# a = zip(lst1, lst2, lst3)
# print("__iter__" in dir(a))
# for item in a:
#     print(item)


lst1 = ["胡辣汤", "疙瘩汤", "紫菜蛋花汤"]
lst2 = ["我喜欢吃", "我更喜欢吃", "我不喜欢吃"]

# 可以快速构建字典. 记住
d = dict(zip(lst1, lst2))
print(d)






