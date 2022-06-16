# coding:utf-8
i=0 #统计执行循环的次数
while i<3:  #0,1,2,当i=3时，3<3False,循环执行结束
    user_name=input('请输入您的用户名：')
    pwd=input('请输入您的密码：')
    if user_name=='next' and pwd=='123456':
        print('登陆成功！！！')
        #改变循环条件。退出循环
        i=8 #跳出循环
    else:
        if i<2:
            print('用户名或密码不正确，您还有',2-i,'次机会')
        i+=1
if i==3:
    print('对不起，三次均输入错误!!!')