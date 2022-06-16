# coding:utf-8
#三行四列
for i in range(1,4):
    for j in range(1,5):
        print('*',end='')
    #换行
    print()
print('---------------------------')

#直角三角形
for i in range(1,6):
    for j in range(1,6):
        if i>=j:
            print('*',end='')
    print()
print('---------------------------')

#倒直角三角形
for i in range(1,6):
    for j in range(1,6):
        if i<=j:
            print('*',end='')
    print()