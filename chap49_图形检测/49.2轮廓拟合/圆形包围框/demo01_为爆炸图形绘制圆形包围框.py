# coding:utf-8
import cv2

img=cv2.imread("../../image/shape2.png")   # 读取图片
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   # 转换为灰度图
#对灰度图像进行二值化处理
ret,binary=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
#获取二值化图像中的轮廓及层次
contours,hierarchy=cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
center,radius=cv2.minEnclosingCircle(contours[0])   # 获取轮廓的外接圆
x=int(round(center[0])) # 圆心点横坐标转为近似整数
y=int(round(center[1])) # 圆心点纵坐标转为近似整数
cv2.circle(img,(x,y),int(radius),(0,0,255),2)   # 绘制圆形
cv2.imshow("img",img)   # 显示图像
cv2.waitKey()   # 等待按键
cv2.destroyAllWindows() # 关闭所有窗口