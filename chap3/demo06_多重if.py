# coding:utf-8
score=eval(input('请输入您的成绩：'))
#判断成绩是否合法
if score<0 or score>100:
    print('成绩有误')
elif 0 <= score <60:
    print('E')
elif 0 <= score <70:
    print('D')
elif 70 <= score <80:
    print('C')
elif 80 <= score <90:
    print('B')
else:
    print('A')