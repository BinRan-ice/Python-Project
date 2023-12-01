# coding:utf-8
import urllib.request
import urllib.parse

url='https://www.xslou.com/login.php'
data={
    'username':'18600605736',
    'password':'573656655',
    'action':'login'
}
#发送请求
resp=urllib.request.urlopen(url,data=bytes(urllib.parse.urlencode(data),encoding='utf-8'))
html=resp.read().decode('gbk')  #解码是gbk