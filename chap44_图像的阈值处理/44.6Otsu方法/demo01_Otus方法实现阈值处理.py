# coding:utf-8
import cv2

img=cv2.imread("../image/4.36.jpg")
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
t1,dst1=cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)
#实现Otsu方法的阈值处理
t2,dst2=cv2.threshold(img_gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#在图像上绘制最合适的阈值
cv2.putText(dst2,"best threshold:"+str(2),(0,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
cv2.imshow("BINARY",dst1)
cv2.imshow("OTSU",dst2)
cv2.waitKey()
cv2.destroyAllWindows()