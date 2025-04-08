# coding:utf-8
import cv2

image=cv2.imread('image/4.1.jpg')   #读取图像
px=image[291,218]   #获取像素点(218,291)处的像素值
print("坐标(218,291)处的像素值为：",px)
#获取B通道的值
blue=image[291,218,0]
#获取G通道的值
green=image[291,218,1]
#获取R通道的值
red=image[291,218,2]
print("坐标(218,291)处的像素值为：",blue,green,red)