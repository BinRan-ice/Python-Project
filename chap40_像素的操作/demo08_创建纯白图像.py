# coding:utf-8
import numpy as np
import cv2

width=200   #设置图像的宽度
height=100  #设置图像的高度
#创建指定宽高，单通道，像素值为1的白色图像
img=np.ones((height,width),np.uint8)*255
cv2.imshow("image",img) #显示图像
cv2.waitKey()   #等待按键按下
cv2.destroyAllWindows() #关闭所有窗口
