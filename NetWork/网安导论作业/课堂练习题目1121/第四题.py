# coding:utf-8
import numpy as np

Plaintext="hill"
secret_key=np.mat([
    [8,6,9,5],
    [6,9,5,10],
    [5,8,4,9],
    [10,6,11,4]
])
plaintext_lst=[]    #存储明文对应的字符

#构造字母数字对应表
chart={}    #数字字母对应表
for i in range(26):
    chart[i]=chr(i+97)

#将明文转换成对应的一阶矩阵
for i in Plaintext:
    for key ,value in chart.items():
        if i==value:
            plaintext_lst.append(key)
plaintext_lst_matrix=np.matrix(plaintext_lst)

#将明文转换成密文
result1=np.dot(plaintext_lst_matrix,secret_key)
result2=result1%26
result3=np.matrix.tolist(result2)[0]
print(result3)
result=[]
for item in result3:
    result.append(chart[item])
print("".join(result))
