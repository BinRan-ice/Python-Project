# coding:utf-8
import cv2

img=cv2.imread("../image/4.27.png")
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#选取两种不同的自适应阈值的计算方法
athdMEAM=cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,3)
athdGAUS=cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,3)
cv2.imshow("MEAN_C",athdMEAM)
cv2.imshow("GAUSSIAN_C",athdGAUS)
cv2.waitKey()
cv2.destroyAllWindows()