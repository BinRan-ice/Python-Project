# coding:utf-8
#统计字符串中指定字符出现的次数
s='HelloPython,HelloJava,hellophp'
word=input('请输入您要统计的字符：')
print('{0}在{1}中一共出现了{2}次'.format(word,s,s.upper().count(word)))