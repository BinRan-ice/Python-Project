# coding:utf-8
#倒直角三角形
for i in range(1,6):
    for j in range(1,6):
        if i<=j:
            print('*',end='')
    print()

#等腰三角形
'''
&&&&*
&&&***
&&*****
&*******
*********
'''
print('------------------------')
for i in range(1,6):
    #倒三角形
    for j in range(1,6-i):
        print(' ',end='')
    #1,,5,7,9的三角形
    for k in range(1,2*i):
        print('*',end='')
    print()
