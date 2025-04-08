# coding:utf-8
import cv2

image=cv2.imread('image/3.1.jpg',0) #显示灰度图像
cv2.imshow("flower",image)
#按下任意键关闭显示窗口
cv2.waitKey(5000)   #设置显示时间为5秒
cv2.destroyAllWindows()