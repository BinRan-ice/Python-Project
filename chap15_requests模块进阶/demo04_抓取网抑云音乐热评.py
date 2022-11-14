# coding:utf-8
import requests
import json
from Crypto.Cipher import AES
from base64 import b64encode

"""
1.找到未加密的数据                          windows.arsea(参数,xxx,xxx,xxx,xxx)
2.想办法把参数进行加密（必须参考网易云的逻辑），params=>encText，encSeckey=>encSeckey
3.请求网易，拿到评论
"""

url="https://music.163.com/weapi/comment/resource/comments/get?csrf_token="
#请求方式POST
data={
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_1325905146",
    "threadId": "R_SO_4_1325905146"
}

#服务于d的
f="00e0b509f6259df8642dbc35662901477df22677ec152b" \
  "5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e41" \
  "7629ec4ee341f56135fccf695280104e0312ecbda92557" \
  "c93870114af6c9d05c4f7f0c3685b7a46bee255932575c" \
  "ce10b424d813cfe4875d3e82047b97ddef52741d546b8e" \
  "289dc6935b3ece0462db0a22b8e7"
g="0CoJUm6Qyw8W8jud"
e="010001"
i="nHav4IJ69xM50avp"        #手动固定的

def get_encSecKey():        #由于i是固定的，那么encSecText就是固定的，c（）函数的结果就是固定的
    return "35b784e309f688356f3a57606736db0096b75208e10165496fe7a31edb036b4dea68a0326a14470e75afe85955e2fb252fa5edc7153479732d8cfd114753e245cb639e279a4e1c5f5733ccf80f85279a585e905be457268b14431aaa508a682d3865f0af470b669e36578d4c8cbcfb09475b28d81f78d1e667a46a6a58cece8c"

#把参数进行加密
def get_params(data):       #默认这里接受的是字符串
    first=enc_params(data,g)
    second=enc_params(first,i)
    return second       #返回params

#转化成16的倍数，为下方的加密算法服务
def to_16(data):
    pad=16-len(data)%16
    data+=chr(pad)*pad
    return data

#加密过程
def enc_params(data,key):
    iv="0102030405060708"
    data=to_16(data)
    aes=AES.new(key=key.encode("utf-8"),IV=iv.encode("utf-8"),mode=AES.MODE_CBC)   #创造加密器
    bs=aes.encrypt(data.encode("utf-8"))   #加密,加密的内容的长度必须是16的倍数
    #处理字节返回字符串
    return str(b64encode(bs),"utf-8")       #转化成字符串返回

#处理加密过程
"""
function a(a=16) {  #随机的十六位字符串
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)      
            e = Math.random() * b.length,       #循环16次，随机数
            e = Math.floor(e),      #取整数
            c += b.charAt(e);       #取字符串中的xxx位置
        return c
    }
    function b(a, b) {  #a=要加密的内容
        var c = CryptoJS.enc.Utf8.parse(b)  #b是密钥
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)      #e是数据
          , f = CryptoJS.AES.encrypt(e, c, {    #c加密密钥
            iv: d,  #偏移量
            mode: CryptoJS.mode.CBC #模式：cbc
        });
        return f.toString()
    }
    function c(a, b, c) {       #c里面不产生随机数
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {    d:数据    e:010001     f:很长   g:0CoJUm6Qyw8W8jud
        var h = {}      空对象
          , i = a(16);  16位随机值，把i设置成定值
        h.encText = b(d, g)     #g是密钥
        h.encText = b(h.encText, i)     返回的就是params     i是密钥
        h.encSecKey = c(i, e, f)        返回的就是encSeckey,e和f是定死的值，如果此时把i固定，key既是固定的
        return h
    }

    两次加密：
    数据+g => b => 第一次加密+i => b => params
"""

#发送请求，得到评论结果
resp=requests.post(url,data={
    "params":get_params(json.dumps(data)),
    "encSecKey":get_encSecKey()
})
print(resp.text)
resp.close()
