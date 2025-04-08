# coding:utf-8
import cv2
import numpy as np
import math

image=cv2.imread("../image/image_map.png")
templ=cv2.imread("../image/templ-1.png")
height,width,c=templ.shape
results=cv2.matchTemplate(image,templ,cv2.TM_CCOEFF_NORMED)     #按照标准相关系数匹配
point_X=[]      #用于存储最佳匹配结果左上角横坐标的列表
point_Y=[]      #用于存储最佳匹配结果左上角纵坐标的列表

for y in range(len(results)):
    for x in range(len(results[y])):
        if results[y][x]>0.99:
            cv2.rectangle(image,(x,y),(x+width,y+height),(255,0,0),2)
            point_X.extend([x])
            point_Y.extend([y])

#出发点的横纵坐标
start_X=62
start_Y=150
#计算出发点到人民广场地铁站的距离
place_Square=np.array([point_X[0],point_Y[0]])
place_Start=np.array([start_X,start_Y])
minus_SS=place_Start-place_Square
print(minus_SS)
start_Square=math.hypot(minus_SS[0],minus_SS[1])
print(start_Square)
#计算出发点到解放大路地铁站的距离
place_Highroad=np.array([point_X[1],point_Y[1]])
minus_HS=place_Highroad-place_Start
start_Highroad=math.hypot(minus_HS[0],minus_HS[1])
#用绿色的线画出距离较短的路线：
if start_Square<start_Highroad:
    cv2.line(image,(start_X,start_Y),(point_X[0],point_Y[0]),(0,255,0),2)
else:
    cv2.line(image, (start_X, start_Y), (point_X[1], point_Y[1]), (0, 255, 0), 2)
cv2.imshow("img",image)
cv2.waitKey()
cv2.destroyAllWindows()