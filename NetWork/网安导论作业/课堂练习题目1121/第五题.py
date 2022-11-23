# coding:utf-8
'''
仿射密码K = (a,b)
加密函数是E(x)= (ax + b) (mod 26)
解密函数为D(x) = (a^-1)(x - b) (mod 26)，其中a^-1是a的乘法逆元
'''

# 遍历得到a的乘法逆元
def get_multiplicative_inverse(a):
    for i in range(1, 27):
        if a * i % 26 == 1:
            return i

# 解密
def dec(a, b, ciphertext):
    a_mul_inv = get_multiplicative_inverse(a)
    p = []
    for i in ciphertext:
        temp = (((ord(i) - 97) - b) * a_mul_inv) % 26 + 97
        p.append(chr(temp))
    print(''.join(p).upper())


if __name__ == "__main__":
    a, b = 7, 3
    ciphertext='FMXVEDKAPHFERBNDKRXRSREFMORUDSDKDVSHVUFEDKAPRKDLYEVLRHHRH'.lower()
    dec(a, b, ciphertext)
