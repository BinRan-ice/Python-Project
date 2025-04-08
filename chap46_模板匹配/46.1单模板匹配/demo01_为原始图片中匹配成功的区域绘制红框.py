# coding:utf-8
import cv2

img=cv2.imread("../image/background.jpg")
templ=cv2.imread('../image/template.png')
height,width,c=templ.shape
#按照标准平方差方式匹配
results=cv2.matchTemplate(img,templ,cv2.TM_SQDIFF_NORMED)
#获取匹配结果中的最小值，最大值，最小值坐标和最大值坐标
minValue,maxValue,minLoc,maxLoc=cv2.minMaxLoc(results)
#将最小值坐标当做最佳匹配区域的左上角坐标
resultPoint1=minLoc
#计算出最佳匹配区域的右下角点坐标
resultPoint2=(resultPoint1[0]+width,resultPoint1[1]+height)
#在最佳匹配区域位置绘制红色方框，线宽为2像素
cv2.rectangle(img,resultPoint1,resultPoint2,(0,0,255),2)
cv2.imshow("img",img)
cv2.waitKey()
cv2.destroyAllWindows()