# coding:utf-8
import cv2

img=cv2.imread("../image/flower.png")   # 读取图片
cv2.imshow("img",img)   # 显示原图
img=cv2.medianBlur(img,5)   # 中值滤波
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   # 转换为灰度图
ret,binary=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)   # 二值化
cv2.imshow("binary",binary)   # 显示二值化后的图像
#获取二值化图像中的轮廓及层次
contours,hierarchy=cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img,contours,-1,(0,0,255),2)   # 绘制所有轮廓
cv2.imshow("contours",img)   # 显示图像
cv2.waitKey()   # 等待按键
cv2.destroyAllWindows() # 关闭所有窗口