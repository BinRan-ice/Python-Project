# coding:utf-8
#文件修改操作
"""
读取文件中的内容
把要修改的内容进行修改
把新内容写入到一个副本文件中

必须借助os模块
把原来的文件删除
把新文件重命名成原来的文件名
"""
import os
with open("f.txt", mode= "r", encoding= "utf-8") as f1, \
    open("f_副本.txt", mode="w", encoding="utf-8") as f2:
    for line in f1:
        if "阿拉斯加" in line:
            line = line. replace("阿拉斯加","人")
        f2.write(line)
os. remove("f.txt") # 删除源文件
os. rename("f_副本.txt", "f.txt") # 把副本文件重命名成源文件

#读取规则的文件
f=open("g.txt",mode="r",encoding="utf-8")
head_str=f.readline()
#把头处理成列表
head_list=head_str.split()      #默认的split()用空白切割
print(head_list)
lst=[]
for line in f:
    line=line.strip()       #去除左右两段空白
    data_list=line.split()      #切割
    print(data_list)
    dic={}
    for i in range(len(head_list)):     #拿到索引
        dic[head_list[i]]=data_list[i]  #向字典中填充数据
    lst.append(dic)
print(lst)
f.close()