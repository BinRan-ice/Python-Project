fp=open('text.txt','w',encoding='utf-8')    #打开文件
print("人生苦短，我用python",file=fp)  #向文件中写入内容
fp.close()  #关闭文件