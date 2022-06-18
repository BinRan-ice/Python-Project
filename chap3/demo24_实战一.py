# coding:utf-8
year=eval(input('请输入一个四位的年份：'))
if (year%4==0 and year%100!=0) or (year%400==0):
    print(year,'年是闰年')
else:
    print(year,'年是平年')