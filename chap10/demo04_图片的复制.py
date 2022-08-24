# coding:utf-8
src_file=open('logo.png','rb')
target_file=open('copylogo.png','wb')
target_file.write(src_file.read())
target_file.close()
src_file.close()

'''
方法二：
with open('logo.png','rb') as src_file:
    with open('copylogo.png','wb') as target_file:
        target_file.write(src_file.read())
'''