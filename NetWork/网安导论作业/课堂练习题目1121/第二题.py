# coding:utf-8

Plaintext="please keep this message in secret"
secret_key="computer"
secret_key_len=len(secret_key)
ciphertext=''
lst1=[]
lst2=[]
count=0
for i in range(97,123):
    lst2.append(chr(i))
for j in range(0,26):
    lst1.append(lst2[j:]+lst2[0:j])
for s in Plaintext:
    if s == " ":
        ciphertext+=s
    else:
        (count % len(secret_key) - 97)
        ciphertext+=lst1[ord(s)-97][ord(secret_key[count%secret_key_len])-97]
        count+=1
print(ciphertext)