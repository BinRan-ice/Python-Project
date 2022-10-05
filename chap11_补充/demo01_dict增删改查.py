# coding:utf-8
#练习：[11,22,33,44,55,66,77,88,99]
#将大于50的放一起，将小于50的放一起


#方法一：
lst=[11,22,33,44,55,66,77,88,99]
result={}       #结果
for item in lst:        #遍历每一个数字
    if item>50:
        if result.get('bigger') ==None:
            result['bigger'] = [item]       #没有bigger，创建一个列表扔进去
        else:
            result['bigger'].append(item)   #有这个列表，添加
    else:
        if result.get('smaller') ==None:
            result['smaller'] = [item]       #没有smaller，创建一个列表扔进去
        else:
            result['smaller'].append(item)   #有这个列表，添加
print(result)


#方法二：
lst2=[11,22,33,44,55,66,77,88,99]
result2={}

for item in lst2:
    if item>50:
        result2.setdefault("bigger",[]).append(item)
    else:
        result2.setdefault("smaller", []).append(item)
print(result2)