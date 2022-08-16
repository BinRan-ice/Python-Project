# coding:utf-8
def get_sum(num):
    s=0
    for i in range(1,num+1):
        s+=i
    print(f'1到{num}之间的和为：{s}')

#函数的调用
get_sum(10)
get_sum(100)