# coding:utf-8
#创建一个列表，用于存储用户商品信息
lst=[]
for i in range(5):
    goods=input("请输入商品的编号和商品的名称，进行商品入库，每次只能输入一件商品：")
    lst.append(goods)
#输出所有商品信息
for item in lst:
    print(item)

#创建一个空列表：
cart=[]
while True:
    flag=False  #代表没有商品的情况
    num=input('请输入要购买的商品编号：')
    #遍历商品列表查询一下购买的商品是否存在
    for item in lst:
        if num ==item[:4]:
            flag=True
            cart.append(item)   #添加到购物车列表
            print('商品已添加到购物车')
            break
    if flag==False and num!='q':    #简写not flag
        print('该商品不存在！！！')
    if num =='q':
        break   #退出while循环
print('您购物车里已选择的商品为：')
#反向
cart.reverse()
for item in cart:
    print(item)