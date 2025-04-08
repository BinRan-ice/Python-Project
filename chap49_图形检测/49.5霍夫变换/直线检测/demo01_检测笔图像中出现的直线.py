# coding:utf-8
import cv2
import numpy as np

img=cv2.imread("../../image/pen.jpg")   # 读取图片
o=img.copy()  # 复制原图
o=cv2.medianBlur(o,5)  # 中值滤波
gray=cv2.cvtColor(o,cv2.COLOR_BGR2GRAY)  # 转换为灰度图
binary=cv2.Canny(o,50,150)  # 边缘检测
#检测直线，精度为1，全角度，阈值为15，线段最短为100，最小间隔为18
lines=cv2.HoughLinesP(binary,1,np.pi/180,15,minLineLength=100,maxLineGap=18)
for line in lines:  # 遍历每一条线
    x1,y1,x2,y2=line[0]  # 获取线的端点
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)  # 绘制直线
cv2.imshow("img",img)  # 显示图像
cv2.imshow("canny",binary)  # 显示边缘检测后的图像
cv2.waitKey()  # 等待按键
cv2.destroyAllWindows() # 关闭所有窗口