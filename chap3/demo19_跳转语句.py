# coding:utf-8
#1+2+3+4+5+6
s=0 #存储累加和
i=1
while i<11:
    s+=i
    if s>=20:
        print('累加和大于20的当前数是：',i)
        break
    i+=1

print('------------------')
i=0
while i<3:
    user_name=input('请输入用户名：')
    pwd=input('请输入密码：')
    if user_name=='next' and pwd=='888888':
        print('登陆成功！！！')
        break
    else:
        if i < 2:
            print('用户名或密码不正确，您还有', 2 - i, '次机会')
        i += 1
else:
    print('对不起，三次均输入错误!!!')