# coding:utf-8
import cv2

img=cv2.imread("../image/demo.png")    # 读取图像
rows,cols=img.shape[:2] # 获取图像的行数与列数
center=(cols/2,rows/2)  # 获取图像的中心点
M=cv2.getRotationMatrix2D(center,30,0.8)    # 以图像的中心点进行逆时针旋转30度，缩放比例为0.8
dst=cv2.warpAffine(img,M,(cols,rows))    # 对图像进行旋转
cv2.imshow("img",img)   # 显示原图像
cv2.imshow("dst",dst)   # 显示旋转后的图像
cv2.waitKey()   # 等待按键按下
cv2.destroyAllWindows() # 关闭所有窗口