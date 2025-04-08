# coding:utf-8
import cv2

img = cv2.imread('../image/amygdalus triloba.jpg')  # 读取图片
dst1=cv2.GaussianBlur(img,(15,15),0)  # 使用15x15的滤波核进行高斯滤波
#双边滤波，选取范围直径为15，颜色差为120
dst2=cv2.bilateralFilter(img,15,120,100)
cv2.imshow("img", img)  # 显示原图
cv2.imshow("Gauss", dst1)  # 显示高斯滤波后的图像
cv2.imshow("bilateral", dst2)  # 显示双边滤波后的图像
cv2.waitKey()
cv2.destroyAllWindows()