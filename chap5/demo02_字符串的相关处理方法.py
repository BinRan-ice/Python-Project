# coding:utf-8
s='HelloWorld'
#字符串的替换
new_s=s.replace('o','你好')

#字符串在指定的宽度范围内居中
print(s.center(20))
print(s.center(20,'*'))

#去除字符串左右的空格
s='   Hello   World   '
print(s.strip())    #结果是一个新的字符串
print(s.lstrip())   #去除字符串左侧的空格
print(s.rstrip())   #去除字符串右侧的空格

#去除指定的字符
s3='dlHelloWorld'
print(s3.strip('ld'))   #与顺序无关，dl还是ld，只要左右包含l，d就去掉
print(s3.lstrip('ld'))
print(s3.rstrip('ld'))