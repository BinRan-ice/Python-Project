# coding:utf-8
d={'hello':10,'world':20,'python':30}
#访问字典中的元素
#(1)使用[key]
print(d['hello'])
print(d['world'])
#(2)使用d.get(key
print(d.get('python'))

#二者之间是有区别的  如果key不存在，d[key]会报错，d.get()可以指定默认值
#print(d['java'])    #KeyError: 'java'
print(d.get('java'))    #None
print(d.get('java','不存在'))

#字典的遍历
for element in d.items():
    print(element)  #结果是一个元组类型-->key-value

#在使用for循环遍历时，分别获取key和value
for key,value in d.items():
    print(key,'-->',value)