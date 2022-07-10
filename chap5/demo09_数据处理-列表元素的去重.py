# coding:utf-8
lst=['金星','木星','水星','火星','金星','木星','水星','火星','金星','木星','水星','火星']
new_lst=[]
#(1)遍历+not in
for item in lst:
    if item not in new_lst:
        new_lst.append(item)
print(new_lst)

#(2)索引+not in
new_lst2=[]
for i in range(len(lst)):
    if lst[i] not in new_lst2:
        new_lst2.append(lst[i])
print(new_lst2)

#(3)使用集合去重
s_lst=set(lst)
new_lst3=list(s_lst)
new_lst3.sort(key=lst.index)
print(new_lst3)