# coding:utf-8
a=[10,20,30]
b=[10,20,30]

print(a==b)     #True,判断两个内容的值是否一致
print(a is b)   #False,判断两个内容的内容地址是否一致

print(id(a))
print(id(b))

#一般我们用is来判空
c=None
if c is None:
    print("c是空")
else:
    print("c不是空")