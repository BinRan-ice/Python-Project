# coding:utf-8
s='helloworldhelloworlddwdnwindiwcnidcnis'
#(1)字符串的拼接及not in判断
new_s=''
for item in s:
    if item not in new_s:
        new_s+=item
print(new_s)

#(2)使用索引+not in
new_s2=''
for i in range(len(s)):
    if s[i] not in new_s2:
        new_s2+=s[i]
print(new_s2)

#(3)通过集合去重_列表排序
new_s3=set(s)
lst=list(new_s3)
print(lst.sort(key=s.index))    #排序的关键字
print(''.join(lst))