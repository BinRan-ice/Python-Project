# coding:utf-8
import cv2

img = cv2.imread("image/5.1.jpg")  # 读取图像
cv2.imshow("image", img)  # 显示图像
# 将图像从BGR色彩空间转换到GRAY色彩空间
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    #转换色彩空间
cv2.imshow("image_gray", img_gray)  # 显示图像
# 将图像从GRAY色彩空间转换到BGR色彩空间,如果是灰色图像则无法恢复成彩色图像
# ss=cv2.cvtColor(img_gray,cv2.COLOR_GRAY2BGR)    #转换色彩空间
# cv2.imshow("ss",ss)
cv2.waitKey()  # 等待按键按下
cv2.destroyAllWindows()  # 关闭所有窗口
