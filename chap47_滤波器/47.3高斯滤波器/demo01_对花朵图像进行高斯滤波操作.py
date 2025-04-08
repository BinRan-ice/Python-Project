# coding:utf-8
import cv2

img = cv2.imread('../image/amygdalus triloba.jpg')  # 读取图片
dst1=cv2.GaussianBlur(img,(5,5),0)  # 使用5x5的滤波核进行高斯滤波
dst2=cv2.GaussianBlur(img,(9,9),0)  # 使用9x9的滤波核进行高斯滤波
dst3=cv2.GaussianBlur(img,(15,15),0)  # 使用15x15的滤波核进行高斯滤波
cv2.imshow("img", img)  # 显示原图
cv2.imshow("5", dst1)  # 显示高斯滤波后的图像
cv2.imshow("9", dst2)  # 显示高斯滤波后的图像
cv2.imshow("15", dst3)  # 显示高斯滤波后的图像
cv2.waitKey()
cv2.destroyAllWindows()