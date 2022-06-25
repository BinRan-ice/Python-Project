# coding:utf-8
lst=[4,45,56,76,1,89,65,33,90]
print('原列表：',lst)
#排序，默认是升序
lst.sort()
print(lst)

#排序，降序
lst.sort(reverse=True)
print("降序:",lst)

print('-----------------------')
lst2=['banana','apple','cat','orange']
print('原列表：',lst2)
#升序排序   先排大写，再排小写
lst2.sort()
print('升序:',lst2)
#降序
lst2.sort(reverse=True)
print('降序:',lst2)
#忽略大小写进行比较
lst2.sort(key=str.lower,reverse=True)
print(lst2)