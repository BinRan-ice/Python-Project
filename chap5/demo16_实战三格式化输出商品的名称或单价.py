# coding:utf-8
lst=[
    ['01','电风扇','美的',500],
    ['02','洗衣机','TCL',1000],
    ['03','微波炉','老板',400]
]
print('编号\t\t名称\t\t\t品牌\t\t单价')
for item in lst:
    for i in item:
        print(i,end='\t\t')
    print()

#格式化
for item in lst:
    item[0]='0000'+item[0]
    item[3]='￥{:.2f}'.format(item[3])
print('*'*50)
#重新遍历列表
print('编号\t\t\t名称\t\t\t品牌\t\t单价')
for item in lst:
    for i in item:
        print(i,end='\t\t')
    print()