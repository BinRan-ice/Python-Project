# coding:utf-8
import cv2

img=cv2.imread("../image/car.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
t1,dst1=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
t2,dst2=cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow("img",img)
cv2.imshow("gray",gray)
cv2.imshow("dst1",dst1)
cv2.imshow("dst2",dst2)
cv2.waitKey()
cv2.destroyAllWindows()