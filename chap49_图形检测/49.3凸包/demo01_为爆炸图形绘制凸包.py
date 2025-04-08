# coding:utf-8
import cv2

img=cv2.imread("../image/shape2.png")   # 读取图片
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   # 转换为灰度图
ret,binary=cv2.threshold(gray,127,225,cv2.THRESH_BINARY)    # 二值化
#获取二值化图像中的轮廓及层次
contours,hierarchy=cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
hull=cv2.convexHull(contours[0])   # 获取轮廓的凸包
cv2.polylines(img,[hull],True,(0,0,255),2)   # 绘制凸包
cv2.imshow("img",img)   # 显示图像
cv2.waitKey()   # 等待按键
cv2.destroyAllWindows() # 关闭所有窗口