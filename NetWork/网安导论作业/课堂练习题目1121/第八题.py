# coding:utf-8
#扩展欧几里得算法
def ext_gcd(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, gcd = ext_gcd(b, a % b) #递归直至余数等于0(需多递归一层用来判断)
        x, y = y, (x - (a // b) * y) #辗转相除法反向推导每层a、b的因子使得gcd(a,b)=ax+by成立
        return x, y, gcd

if __name__ == '__main__':
    a=0X4E
    b=int('100011011',2)
    answer=list(ext_gcd(a,b))
    print(hex(answer[0]))