# coding:utf-8
s=0
for i in range(1,101):
    if i % 2 == 0:
        s += i
        i += 1
    else:
        i += 1
        continue
print('1-100之间的偶数和为：',s)