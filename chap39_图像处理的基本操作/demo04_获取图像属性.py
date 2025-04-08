# coding:utf-8
import cv2

image_Color=cv2.imread('image/3.1.jpg')   #读取图像
print("获取彩色图像的属性：")
print("shape=",image_Color.shape)   #获取图像的形状(垂直像素数，水平像素数，通道数)
print("size=",image_Color.size)     #获取图像的像素数目
print("dtype=",image_Color.dtype)   #获取图像的数据类型
image_Gray=cv2.imread('image/3.1.jpg',0)   #读取灰度图像
print("获取灰度图像的属性：")
print("shape=",image_Gray.shape)   #获取图像的形状(垂直像素数，水平像素数，通道数)
print("size=",image_Gray.size)     #获取图像的像素数目
print("dtype=",image_Gray.dtype)   #获取图像的数据类型