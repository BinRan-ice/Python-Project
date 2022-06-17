# coding:utf-8
row=eval(input('请输入菱形的行数：'))
while row%2==0:
    row = eval(input('重新输入菱形的行数：'))
top_row=(row+1)//2
#上半部分
for i in range(1,top_row+1):
    #倒三角形
    for j in range(1,top_row+1-i):
        print(' ',end='')
    #1,,5,7,9的三角形
    for k in range(1,2*i):
        if k==1 or k==i*2-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()

#下半部分
bottom_row=row//2
for i in range(1,bottom_row+1):
    #直角三角形
    for j in range(1,i+1):
        print(' ',end='')
    for k in range(1,2*(bottom_row-i+1)): #(1,7) (2,5) (3,3) (4,1)
        if k==1 or k==2*(bottom_row-i+1)-1:
            print("*",end='')
        else:
            print(' ',end='')
    print()