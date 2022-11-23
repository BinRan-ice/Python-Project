# coding:utf-8
# coding:utf-8
import numpy as np

def answer_secret_key(secret_key,Plaintext,chart):
    plaintext_lst=[]    #存储明文对应的字符

    #将明文转换成对应的一阶矩阵
    for i in Plaintext:
        for key ,value in chart.items():
            if i==value:
                plaintext_lst.append(key)
    plaintext_lst_matrix=np.matrix(plaintext_lst)
    #print(plaintext_lst_matrix)

    #将明文转换成密文
    result1=np.dot(plaintext_lst_matrix,secret_key)
    result2=result1%26
    result3=np.matrix.tolist(result2)[0]
    #print(result3)
    result=[]
    for item in result3:
        result.append(chart[item])
    answer="".join(result)
    return answer

if __name__ == '__main__':
    Plaintext="Friday".lower()
    ciphertext = 'POCFKU'.lower()
    Plaintext1=Plaintext[:2]
    Plaintext2=Plaintext[2:4]
    Plaintext3=Plaintext[4:6]
    # 构造字母数字对应表
    chart = {}  # 数字字母对应表
    for i in range(26):
        chart[i] = chr(i + 97)
    for i in range(20):
        for j in range(20):
            for m in range(20):
                for n in range(20):
                    count=0
                    secret_key=np.mat([
                        [i,j],
                        [m,n]
                    ])
                    ciphertext1=answer_secret_key(secret_key,Plaintext1,chart)
                    ciphertext2=answer_secret_key(secret_key,Plaintext2,chart)
                    ciphertext3=answer_secret_key(secret_key,Plaintext3,chart)
                    test_ciphertext=ciphertext1+ciphertext2+ciphertext3
                    for k in range(len(test_ciphertext)):
                        if test_ciphertext[k]==ciphertext[k]:
                            count+=1
                    if count>=5:
                        print(test_ciphertext.upper(),secret_key)
