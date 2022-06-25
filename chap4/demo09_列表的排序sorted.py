# coding:utf-8
lst=[4,45,56,76,1,89,65,33,90]
print('原列表：',lst)
#排序
asc_lst=sorted(lst)
print('升序:',asc_lst)
print('原列表：',lst)

#降序
desc_lst=sorted(lst,reverse=True)
print('降序:',desc_lst)
print('原列表：',lst)

lst2=['banana','apple','cat','orange']
print('原列表：',lst2)

#忽略大小写的排序
new_lst2=sorted(lst2,key=str.lower)
print('原列表:',new_lst2)