# coding:utf-8
import cv2
import numpy as np

#水平拼接
a=np.array([1,2,3])
b=np.array([4,5,6])
c=np.array([7,8,9])
result1=np.hstack((a,b,c))
print(result1)

#垂直拼接
result2=np.vstack((a,b,c))
print(result2)

#按照水平和垂直两种方式拼接两幅图像
img=cv2.imread('image/stone.jpg')   #读取图像
img_h=np.hstack((img,img)) #水平拼接
img_v=np.vstack((img,img)) #垂直拼接
cv2.imshow('img_h',img_h)   #显示水平拼接后的图像
cv2.imshow('img_v',img_v)   #显示垂直拼接后的图像
cv2.waitKey()   #等待按键按下
cv2.destroyAllWindows() #关闭所有窗口