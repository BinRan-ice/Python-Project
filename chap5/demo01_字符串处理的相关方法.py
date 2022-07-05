# coding:utf-8
#大小写转换
s1='HelloWorld'
new_s2=s1.lower()   #全部转成小写
print(s1,new_s2)
new_s3=s1.upper()   #全部转成大写
print(s1,new_s3)

#字符串的分割
s_email='next@126.com'
lst=s_email.split('@')
print('邮箱名：',lst[0],'邮件服务器域名：',lst[1])

#统计子串在指定字符串出现的个数
print(s1.count('o'))    #表示o出现了两次

#检索操作--查询
print(s1.find('o')) #o首次出现的位置
print(s1.find('p')) #没找到结果为-1

print(s1.index('o'))    #o首次出现的位置
#print(s1.index('p'))    #ValueError: substring not found

#判断前缀和后缀
print(s1.startswith('H'))
print(s1.startswith('p'))
print(s1.endswith('d'))
print(s1.endswith('p'))

print('demo.py'.endswith('.py'))
print('text.txt'.endswith('.txt'))
