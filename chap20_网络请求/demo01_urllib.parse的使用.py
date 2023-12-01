# coding:utf-8
import urllib.parse
kw={'wd':'汉字'}
#编码
result=urllib.parse.urlencode(kw)
print(result)
#解码
res=urllib.parse.unquote(result)
print(res)