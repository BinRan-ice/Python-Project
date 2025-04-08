# coding:utf-8
import cv2

img=cv2.imread("../image/flower.png")   # 读取图片
r1=cv2.Canny(img,10,50)  # 使用不同阈值进行Canny边缘检测
r2=cv2.Canny(img,100,200)
r3=cv2.Canny(img,400,600)
cv2.imshow("r1",r1)  # 显示Canny边缘检测的结果
cv2.imshow("r2",r2)
cv2.imshow("r3",r3)
cv2.imshow("img",img)  # 显示原图
cv2.waitKey()  # 等待按键
cv2.destroyAllWindows() # 关闭所有窗口