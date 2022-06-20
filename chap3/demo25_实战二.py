# coding:utf-8
#(1)初始化变量
answer='y'
#(2)条件判断
while answer=='y':
    print('---------------欢迎使用10086查询功能----------------')
    print('1.查询当前余额')
    print('2.查询当前剩余流量')
    print('3.查询当前剩余的通话时长')
    print('0.退出系统')
    choice=input('请输入您要执行的操作：')
    if choice=='1':
        print('当前余额为：234.5')
    elif choice=='2':
        print('当前剩余流量为：10.5G')
    elif choice=='3':
        print('当前的剩余通话时长为：200分钟')
    elif choice=='0':
        print('程序退出，感谢您的使用')
    else:
        print('对不起，您输入的有误，请重新输入')
    #（4）改变变量
    answer=input('还要继续操作么？y/n')
else:
    print('程序退出，谢谢使用')