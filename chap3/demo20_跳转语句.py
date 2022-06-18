# coding:utf-8
for i in range(1,4):
    user_name = input('请输入用户名：')
    pwd = input('请输入密码：')
    if user_name == 'next' and pwd == '888888':
        print('登陆成功！！！')
        break
    else:
        if i < 2:
            print('用户名或密码不正确，您还有', 2 - i, '次机会')
else:
    print('对不起，三次均输入错误!!!')

print('---------------')
for i in 'hello':
    if i=='e':
        break
    print(i)