# coding:utf-8
import cv2

image=cv2.imread("../image/image-car.png")
templs=[]
templs.append(cv2.imread("../image/car1.png"))
templs.append(cv2.imread("../image/car2.png"))
templs.append(cv2.imread("../image/car3.png"))
templs.append(cv2.imread("../image/car4.png"))
for car in templs:
    results=cv2.matchTemplate(image,car,cv2.TM_CCOEFF_NORMED)
    for i in range(len(results)):
        for j in range(len(results[i])):
            if results[i][j]>0.99:
                if 0<j<=140:
                    print("车位编号：",1)
                elif j<=330:
                    print("车位编号：",2)
                elif j<=500:
                    print("车位编号：",3)
                else:
                    print("车位编号：",1)
                break
