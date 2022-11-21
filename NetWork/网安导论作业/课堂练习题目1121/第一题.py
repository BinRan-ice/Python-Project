# coding:utf-8

lst1=[1,2,3,4,5,6,7,8]
lst2=[5,1,7,2,6,8,4,3]
new_lst=[]
for i in range(len(lst1)):
    temp1=lst2[i]
    temp2=lst1[temp1-1]
    new_lst.append(lst2[temp2-1])
print(new_lst)

