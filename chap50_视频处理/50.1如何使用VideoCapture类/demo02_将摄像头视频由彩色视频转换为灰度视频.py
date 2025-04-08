# coding:utf-8
import cv2

capture = cv2.VideoCapture(0,cv2.CAP_DSHOW) # 打开笔记本内置摄像头
while (capture.isOpened()): # 笔记本内置摄像头被打开后
    retval, image = capture.read() # 从摄像头中实时读取视频
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # 将彩色图像转换为灰度图像
    if retval == True:  # 如果读取视频成功
        cv2.imshow("Video", image) # 在窗口中显示读取到的视频
        cv2.imshow("Video", image_gray)  # 在窗口中显示读取到的视频
    key = cv2.waitKey(1)
    if key == 32: # 如果按下空格键
        break
capture.release() # 关闭笔记本内置摄像头
cv2.destroyAllWindows() # 销毁显示摄像头视频的窗口