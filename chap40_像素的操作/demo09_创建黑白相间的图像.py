# coding:utf-8
import cv2
import numpy as np

width=200   #设置图像的宽度
height=100  #设置图像的高度
#创建指定宽高，单通道，像素值为0的黑色图像
img=np.zeros((height,width),np.uint8)
for i in range(0,width,40):
    img[:,i:i+20]=255   #将指定区域的像素值设置为255
cv2.imshow("image",img) #显示图像
cv2.waitKey()   #等待按键按下
cv2.destroyAllWindows() #关闭所有窗口