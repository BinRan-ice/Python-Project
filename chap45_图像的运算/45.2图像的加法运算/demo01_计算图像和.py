# coding:utf-8
import cv2

img=cv2.imread("../image/beach.jpg")
sum1=img+img
sum2=cv2.add(img,img)
cv2.imshow("img",img)
cv2.imshow("sum1",sum1)
cv2.imshow("sum2",sum2)
cv2.waitKey()
cv2.destroyAllWindows()