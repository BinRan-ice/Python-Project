# coding:utf-8
s={10,20,30,40,50}
#添加元素
s.add(100)
print(s)

#删除元素
s.remove(40)
print(s)

#清空集合
#s.clear()
#print(s,bool(s))

#遍历集合
for item in s:
    print(item)

for index,item in enumerate(s,1):   #1表示元素开始的序号
    print(index,'-->',item)

#集合的生成式
s={ i for i in range(1,10)}
print(s)

s={i for i in range(1,11) if i%2==0}
print(s)