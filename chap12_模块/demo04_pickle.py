# coding:utf-8
import pickle

lst=["成龙","赵本山","范伟"]
bs=pickle.dumps(lst)
print(bs)

bs=b'\x80\x04\x95#\x00\x00\x00\x00\x00\x00\x00]\x94(\x8c\x06\xe6\x88\x90\xe9\xbe\x99\x94\x8c\t\xe8\xb5\xb5\xe6\x9c\xac\xe5\xb1\xb1\x94\x8c\x06\xe8\x8c\x83\xe4\xbc\x9f\x94e.'
lst=pickle.loads(bs)
print(lst)

"""
dic={"name":"admin","password":123}
f=open("data.txt",mode="w",encoding="utf-8")
f.write(str(dic))
f=open("data.txt",mode="r",encoding="utf-8")
s=f.read()
print(type(s))
d=eval(s)       #eval对安全性有影响
print(d,type(d))
"""

#把数据存储到文件中最合理的方案就是用pickle
dic={"name":"admin","password":123}
pickle.dump(dic,open("d.data",mode="wb"))
#读取序列化之后的文件
dic=pickle.load(open("d.data",mode="rb"))
print(dic)

"""
序列化：把对象转化成二进制字节
反序列化：把二进制字节转化成对象

1.dumps     把对象（数据）转化成字节
2.loads     八字结转化成对象（数据）
3.dump      把对象序列化成字节之后写入文件
4.load      把文件中的字节反序列化成对象
"""