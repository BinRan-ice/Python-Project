# coding:utf-8
s='hello'
s2='world'
print(s+s2) #产生一个新的字符串序列

#注意事项 +左右的数据类型相同，，序列中元素的数据类型可以不同
lst=[10,20,30,'php']
#print(s+lst)    #TypeError: can only concatenate str (not "list") to str
print(s*5)
print('------------------------------')
print('-'*40)