# coding:utf-8
import hashlib

#创建md5对象
obj=hashlib.md5()
#把要加密的信息传递给obj
obj.update("66666".encode("utf-8"))
#从obj中拿到密文
mi=obj.hexdigest()
print(mi)


#正常的默认加密过程是容易撞库的
#解决撞库：加盐
obj=hashlib.md5(b'qoskoqks')
obj.update("66666".encode("utf-8"))
print(obj.hexdigest())

#用户注册
def func(salt,s):
    obj=hashlib.md5(salt)
    obj.update(s.encode("utf-8"))
    return obj.hexdigest()

username=input("请输入用户名：")
password=input("请输入密码：")
#动态加盐
mi_password=func(username.encode("utf-8"),password)
f=open("user.txt",mode="w",encoding="utf-8")
f.write(username)
f.write("\n")
f.write(mi_password)        #把密文写出去

#登录
username=input("请输入用户名：")
password=input("请输入密码：")
password=func(username.encode("utf-8"),password)
f=open("user.txt",mode="r",encoding="utf-8")
uname=f.readline().strip()
upwd=f.readline().strip()
if  username==uname and password==upwd:
    print("登陆成功")
else:
    print("登陆失败")


#文件也可以进行MD5的加密操作
obj=hashlib.md5(b'abcdefg')
f=open("wf.txt",mode="rb")
for line in f:
    obj.update(line)
#得到的加密结果
print(obj.hexdigest())

"""
判断文件一致性
    在我们文件上传的时候，首先计算你要上传的这个文件的MD5，拿着这个值去网盘的数据库中搜索有没有相同的MD5，如果有，直接就是已经上传，已经保存起来了。
"""
