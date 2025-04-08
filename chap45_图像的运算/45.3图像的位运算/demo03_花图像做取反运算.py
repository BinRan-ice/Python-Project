# coding:utf-8
import cv2

flower=cv2.imread("../image/amygdalus triloba.png")
img=cv2.bitwise_not(flower)
cv2.imshow("flower",flower)
cv2.imshow("img",img)
cv2.waitKey()
cv2.destroyAllWindows()