# coding:utf-8
def fac(n):
    if (n==1) or (n==0):
        return 1
    else:
        return n*fac(n-1)

print(fac(6))