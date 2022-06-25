# coding:utf-8
#创建二维列表
lst=[
    ['城市','环比','同比'],
    ['北京',102,103],
    ['上海',100,101],
    ['深圳',100,39]
]
print(lst)
#遍历lst
for row in lst: #行
    for item in row:    #列
        print(item,end='\t')
    print()

#列表生成式生成一个四行五列的列表
lst2=[[j for j in range(5)] for i in range(4)]
print(lst2)