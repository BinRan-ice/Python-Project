# coding:utf-8
#使用{}直接创建
s={10,20,30,40,50}
print(s)
#s1={10,20,[30,40]}   #TypeError: unhashable type: 'list'
#print(s1)
#s={([10,20]),([10,20])} TypeError: unhashable type: 'list'
#print(s)

s={}    #创建的是字典还是集合
print(type(s))  #<class 'dict'>字典

#如何创建一个空集合
s=set()
print(type(s))  #<class 'set'>集合
print(bool(s))

#第二种创建集合的方式set()
s=set("hello")
s2=set([10,20,30])
s3=set(range(1,10))
print(s)
print(s2)
print(s3)

#集合属于序列中的一种
print('max:',max(s))
print('min:',min(s3))
print('len:',len(s3))

print('9在集合中是否存在：',9 in s3)
print('9不在集合中是否存在：',9 not in s3)

#集合的删除
del s3
print(s3)   #NameError: name 's3' is not defined. Did you mean: 's'?