# coding:utf-8
import cv2

img=cv2.imread("../image/shape1.png")   # 读取图片
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   # 转换为灰度图
ret,binary=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)   # 二值化
#监测图像中出现的所有轮廓，记录轮廓的每一个点
#contours,hierarchy=cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
#contours,hierarchy=cv2.findContours(binary,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
contours,hierarchy=cv2.findContours(binary,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)
#绘制所有轮廓，宽度为5，颜色为红色
cv2.drawContours(img,contours,1,(0,0,255),5)
cv2.imshow("img",img)   # 显示图像
cv2.waitKey()   # 等待按键
cv2.destroyAllWindows() # 关闭所有窗口