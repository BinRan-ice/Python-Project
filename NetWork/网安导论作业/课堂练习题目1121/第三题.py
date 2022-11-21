# coding:utf-8

Plaintext = "hide the gold in the tree stump"
secret_key = "cryptography"
lst1 = []  # 密钥矩阵一维
lst2 = []  # 密钥矩阵二维
new_key = ''
ciphertext = ''
count = 0
# 构造密钥矩阵
# 密钥去重
for s in secret_key:
    if s not in new_key:
        new_key += s
for i in range(25):
    if count < len(new_key):
        lst1.append(new_key[count])
        count += 1
    else:
        for i in range(97, 123):
            if chr(i) not in lst1 and chr(i) != 'j':
                lst1.append(chr(i))
for i in range(5):
    lst2.append(lst1[i * 5:(i * 5) + 5])
# 初始化明文
temp_plaintext = Plaintext.replace(" ", "")
temp_plaintext_lst = []
if len(temp_plaintext) % 2 != 0:
    temp_plaintext += 'q'
for i in range(len(temp_plaintext)):
    if i % 2 == 0:
        if temp_plaintext[i] == temp_plaintext[i + 1]:
            temp_plaintext_lst.append(temp_plaintext[i] + 'q')
        else:
            temp_plaintext_lst.append(temp_plaintext[i:i + 2])


# playfair加密明文
# 获取明文在矩阵中的位置
def local(ch, lst2):
    for i in range(len(lst2)):
        for j in range(len(lst2)):
            if ch == lst2[i][j]:
                return i, j


for item in temp_plaintext_lst:
    x1, y1 = local(item[0], lst2)
    x2, y2 = local(item[1], lst2)
    if x1 != x2 and y1 != y2:
        ciphertext += lst2[x1][y2]
        ciphertext += lst2[x2][y1]
    elif x1 == x2:
        if (y2 != (len(lst2) - 1)) and (y1 != (len(lst2) - 1)):
            ciphertext += lst2[x1][y1 + 1]
            ciphertext += lst2[y1][y2 + 1]
        else:
            if y1 == (len(lst2) - 1):
                ciphertext += lst2[x1][y1 % (len(lst2) - 1)]
                ciphertext += lst2[x2][y2 + 1]
            else:
                ciphertext += lst2[x1][y1 + 1]
                ciphertext += lst2[x2][y2 % (len(lst2) - 1)]
    else:
        if (x1 != (len(lst2) - 1)) and (x2 != (len(lst2) - 1)):
            ciphertext += lst2[x1 + 1][y1]
            ciphertext += lst2[x2 + 1][y2]
        else:
            if x1 == (len(lst2) - 1):
                ciphertext += lst2[x1 % (len(lst2) - 1)][y1]
                ciphertext += lst2[x2 + 1][y2]
            else:
                ciphertext += lst2[x1 + 1][y1]
                ciphertext += lst2[x2 % (len(lst2) - 1)][y2]
print(ciphertext)
