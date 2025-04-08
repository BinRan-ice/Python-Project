# coding:utf-8
import cv2

image=cv2.imread('image/4.1.jpg')   #读取图像
cv2.imshow("4.1",image)   #显示图像
for i in range(241,292):
    for j in range(168,219):
        image[i,j]=[255,255,255]    #修改像素点的值
cv2.imshow("4.1_1",image)   #显示图像
cv2.waitKey()
cv2.destroyAllWindows() #关闭窗口