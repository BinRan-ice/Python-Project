# coding:utf-8
#JSON数据存储
import json

s='{"name":"张三"}'
#将字符串转成对象
obj=json.loads(s)
print(obj)

#将对象转换成字符串类型
ss=json.dumps(obj,ensure_ascii=False)
print(ss)

#将对象（dict）保存到文件中
json.dump(obj,open("文件/movie.txt",mode="w",encoding="utf-8"),ensure_ascii=False)
#把文件中的内容读取到python程序
obj2=json.load(open("文件/movie.txt",mode="r",encoding="utf-8"))
print(obj2)
print(type(obj2))