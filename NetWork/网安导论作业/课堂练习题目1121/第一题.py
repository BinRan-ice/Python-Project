# coding:utf-8

lst1=[1,2,3,4,5,6,7,8]
lst2=[5,1,7,2,6,8,4,3]
new_lst=[]
dic=dict(zip(lst2,lst1))
dic=sorted(dic.items(),key=lambda x:x[0])
for item in dic:
    new_lst.append(list(item)[1])
print(new_lst)
