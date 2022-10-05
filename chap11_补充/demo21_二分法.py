# coding:utf-8
lst1=[11,25,46,78,99,265]
n1=int(input(">>>:"))
for item in lst1:
    if item==n1:
        print("存在")
        break
else:
    print("不存在")


#二分法
lst2=[11,22,33,44,55,66,77,88,99]
n2=int(input(">>>:"))
left=0
right=len(lst2)-1       #最大索引号

while left<=right:
    mid=(left+right)//2
    if n>lst2[mid]:
        left=mid+1
    elif n<lst2[mid]:
        right=mid-1
    else:
        print("找到了数据，位置：",mid)
else:
    print("没找到")


#递归版本二分法
lst3=[11,22,33,44,55,66,77,88,99]
n2=int(input(">>>:"))
left=0
right=len(lst3)-1       #最大索引号
def find(lst,n,left,right):
    if left>right:
        print("没找到")
        return
    mid=(left+right)//2
    if n>lst[mid]:
        left=mid+1
    elif n<lst[mid]:
        right=mid-1
    else:
        print("找到了，索引位置",mid)
        return
    find(lst3,n,left,right)     #进入递归