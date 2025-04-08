# coding:utf-8
import numpy as np
import cv2

width=200   #设置图像的宽度
height=100  #设置图像的高度
#创建指定宽高，三通道，随机像素值的图像，随机值范围为0~255，符号为无符号整型
#img=np.random.randint(256,size=(height,width),dtype=np.uint8)
#创建随机彩色图像
img=np.random.randint(256,size=(height,width,3),dtype=np.uint8)
cv2.imshow("image",img) #显示图像
cv2.waitKey()   #等待按键按下
cv2.destroyAllWindows() #关闭所有窗口