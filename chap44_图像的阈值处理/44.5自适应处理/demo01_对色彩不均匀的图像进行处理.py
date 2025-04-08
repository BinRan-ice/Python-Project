# coding:utf-8
import cv2

img=cv2.imread("../image/4.27.png")
#转化为灰度图像
img_gray=cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
#二值化处理
t1,dst1=cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)
#反二值化处理
t2,dst2=cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY_INV)
#低于阈值零处理
t3,dst3=cv2.threshold(img_gray,127,255,cv2.THRESH_TOZERO)
#超出阈值零处理
t4,dst4=cv2.threshold(img_gray,127,255,cv2.THRESH_TOZERO_INV)
#截断处理
t5,dst5=cv2.threshold(img_gray,127,255,cv2.THRESH_TRUNC)
#分别显示经过5种阈值类型处理后的图像
cv2.imshow("BINARY",dst1)
cv2.imshow("BINARY_INV",dst2)
cv2.imshow("TOZERO",dst3)
cv2.imshow("TOZERO_INV",dst4)
cv2.imshow("TRUNC",dst5)
cv2.waitKey()
cv2.destroyAllWindows()