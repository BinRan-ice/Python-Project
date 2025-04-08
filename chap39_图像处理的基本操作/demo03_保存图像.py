# coding:utf-8
import cv2

image=cv2.imread('image/3.1.jpg')   #读取图像
#把图片保存在image目录下
cv2.imwrite('image/3.1_1.jpg',image)