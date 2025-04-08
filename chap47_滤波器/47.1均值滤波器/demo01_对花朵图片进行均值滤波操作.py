# coding:utf-8
import cv2

img = cv2.imread('../image/amygdalus triloba.jpg')  # 读取图片
dst1=cv2.blur(img,(3,3))    #使用大小为3*3的均值滤波器进行滤波
dst2=cv2.blur(img,(5,5))    #使用大小为5*5的均值滤波器进行滤波
dst3=cv2.blur(img,(9,9))    #使用大小为9*9的均值滤波器进行滤波
cv2.imshow('img',img)    #显示原图
cv2.imshow('dst1',dst1)  #显示滤波后的图像
cv2.imshow('dst2',dst2)  #显示滤波后的图像
cv2.imshow('dst3',dst3)  #显示滤波后的图像
cv2.waitKey()
cv2.destroyAllWindows()