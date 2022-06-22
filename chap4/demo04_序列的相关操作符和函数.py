# coding:utf-8
s='helloworld'
print('e在helloworld中存在么？',('e' in s))
print('v在helloworld中存在么？',('v' in s))

print('e不在helloworld中存在么？',('e' not in s))
print('v不在helloworld中存在么？',('v' not in s))

#内置函数
print('len():',len(s))
print('max():',max(s))
print('min():',min(s))

#序列对象的方法
print('s.index',s.index('l'))   #l第一次出现的位置
print('s.count',s.count('l'))   #l出现的次数
