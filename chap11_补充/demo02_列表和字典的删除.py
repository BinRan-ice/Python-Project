# coding:utf-8
lst=["张无忌","张翠山","张三丰","张五侠"]
#删除所有姓张的人
for name in lst:
    if name.startswith('张'):
        lst.remove(name)
print(lst)      #['张翠山', '张五侠']
#循环列表的时候，尽量不要删除，否则删除不干净，当删除某个元素后，列表中的元素会向前移动，如果下一个元素也符合删除规则，则会跳过该元素


#把要删除的内容记录在一个新的列表中，循环这个新列表，删除老列表
#方法一：
lst1=["张无忌","张翠山","张三丰","张五侠"]
new_lst1=[]
for name1 in lst1:
    if name1.startswith("张"):
        new_lst1.append(name1)

for a in new_lst1:
    lst1.remove(a)
print(lst1)

#方法二：
lst2=["张无忌","张翠山","张三丰","张五侠"]
for name2 in lst2[:]:       #lst2[:]是一个浅拷贝，拷贝了一份lst2列表进行操作
    if name2.startswith("张"):
        lst2.remove(name2)
print(lst2)


#字典的删除，再循环字典的时候，删除字典中的数据直接会报错
# dic={"jay":"周杰伦","55k":"卢本伟"}
# for k in dic:
#    dic.pop(k)      #RuntimeError: dictionary changed size during iteration

#把要删除的内容记录在列表中，循环列表，删除字典
dic={"jay":"周杰伦","55k":"卢本伟"}
#把key放在列表中
lst=list(dic.keys())        #拿到字典所有的key，组成一个新的列表
for k in lst:
    dic.pop(k)
print(dic)