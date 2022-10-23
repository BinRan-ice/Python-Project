# coding:utf-8
import json

#1.把python中的字典或者列表，转化成json字符串
dic={"id":1,"name":"我的天啊这么好玩","usertype":0}
s=json.dumps(dic,ensure_ascii=False)    #json处理中文要加ensure_ascii=False
print(s,type(s))

#2.前端返回的json字符串，想办法变成python中的字典
s='{"id":1,"name":"我的天啊这么好玩","usertype":0}'
d=json.loads(s)
print(d,type(d))

"""
dumps:可以把对象转化成json
loads:可以把json转化成对象
"""

#前端的json和python中的字典有什么区别
#{"id": 1, "islogin": true, "hasGirl": null}
d={"id":1,"islogin":True,"hasGirl":None}
print(json.dumps(d))

"""
数据类型的写法不一样
python      前端
True        true
False       false
None        null
"""

#列表一样可以这样直接转化
lst=["哈罗","摩托","春风",True]
s=json.dumps(lst,ensure_ascii=False)
print(s,type(s))

wf={
    "name":"王峰",
    "age":18,
    "hobby":"上头条",
    "wife":{
        "name":"子怡",
        "age":19,
        "hobby":["唱歌","跳舞","演戏"]
    }
}
json.dump(wf,open("wf.txt",mode="w",encoding="utf-8"),ensure_ascii=False)
d=json.load(open("wf.txt",mode="r",encoding="utf-8"))
print(d,type(d))

"""
1.json是一种数据交互的数据格式
2.来自于前端
3.dumps     ensure_ascii=False
4.loads
5.dump      ensure_ascii=False
6.load
"""