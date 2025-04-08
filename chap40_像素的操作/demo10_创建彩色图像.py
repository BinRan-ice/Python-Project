# coding:utf-8
import cv2
import numpy as np

width=200   #设置图像的宽度
height=100  #设置图像的高度
#创建指定宽高，三通道，像素值为0的黑色图像
img=np.zeros((height,width,3),np.uint8)
blue=img.copy() #复制图像
blue[:,:,0]=255    #将蓝色通道的像素值设置为255
green=img.copy()    #复制图像
green[:,:,1]=255    #将绿色通道的像素值设置为255
red=img.copy()  #复制图像
red[:,:,2]=255  #将红色通道的像素值设置为255
cv2.imshow("blue",blue) #显示蓝色通道的图像
cv2.imshow("green",green)   #显示绿色通道的图像
cv2.imshow("red",red)   #显示红色通道的图像
cv2.waitKey()   #等待按键按下
cv2.destroyAllWindows() #关闭所有窗口