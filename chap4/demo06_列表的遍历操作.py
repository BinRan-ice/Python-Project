# coding:utf-8
lst=['hello','world','python','php']
#使用普通那个for循环遍历
for item in lst:
    print(item)

#使用for循环和range()函数和len()函数，根据索引进行遍历
for i in range(len(lst)):
    print(i,'-->',lst[i])

#使用for循环与enumerate()函数,进行遍历
for index,item in enumerate(lst):   #默认序号从0开始
    print(index,item)

for index,item in enumerate(lst,1):   #序号从1开始
    print(index,item)