# coding:utf-8
import cv2
import os
import sys

PIC_PATH="../image/"
width,height=100,100    #缩放比例
pic_file=os.listdir(PIC_PATH)   #所有照片文件列表
same_pic_index=[]   #相同图像的索引列表
imgs=[]     #缩放后的图像对象列表
has_same=set()  #相同图像的集合
count=len(pic_file)     #图片的数量

#如果照片数量为0
if count==0:
    print("没有图像")
    sys.exit(0)

#将所有文件缩放
for file_name in pic_file:
    pic_name=PIC_PATH+file_name
    img=cv2.imread(pic_name)
    img=cv2.resize(img,(width,height))
    imgs.append(img)

for i in range(0,count-1):
    if i in has_same:
        continue
    templ=imgs[i]
    same=[i]    #与temp内容相同的图像索引列表
    for j in range(0+i+1,count):
        if j in has_same:
            continue
        pic=imgs[j]     #取出对照图像
        results=cv2.matchTemplate(pic,templ,cv2.TM_CCORR_NORMED)
        if results[0][0]>0.9:
            same.append(j)
            has_same.add(i)
            has_same.add(j)
    if len(same)>1:
        same_pic_index.append(same)

for same_list in same_pic_index:
    text="相同的照片："
    for same in same_list:
        text+=str(pic_file[same])+","
    print(text)
