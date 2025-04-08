# coding:utf-8

import cv2

img = cv2.imread("image/5.1.jpg")  # 读取图像
# 将图像从BGR色彩空间转换到BGRA色彩空间
img_bgra = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
cv2.imshow("image_bgra", img_bgra)  # 显示图像
b, g, r, a = cv2.split(img_bgra)  # 拆分图像通道
a[:,:]=172  # 将A通道的像素值设置为172
bgra_172=cv2.merge([b,g,r,a])  # 合并图像通道
a[:,:]=0  # 将A通道的像素值设置为0
bgra_0=cv2.merge([b,g,r,a])  # 合并图像通道
cv2.imshow("image_bgra_172", bgra_172)  # 显示图像
cv2.imshow("image_bgra_0", bgra_0)  # 显示图像
cv2.imwrite("image/5.1_bgra_172.png",bgra_172)  # 保存图像
cv2.imwrite("image/5.1_bgra_0.png",bgra_0)  # 保存图像
cv2.waitKey()  # 等待按键按下
cv2.destroyAllWindows()  # 关闭所有窗口