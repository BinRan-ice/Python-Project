# coding:utf-8
s='伟大的中国梦'
#编码 str-->bytes
scode_gbk=s.encode('gbk')
print(scode_gbk)

scode_utf8=s.encode('utf-8')
print(scode_utf8)

#编码中的error处理
s2='helloworld'
scode=s2.encode('gbk',errors='replace') #ignore replace strict

#解码 bytes-->str
print(bytes.decode(scode_gbk,'gbk'))
print(bytes.decode(scode_utf8,'utf-8'))

print(bytes.decode(scode,encoding='gbk',errors='ignore'))