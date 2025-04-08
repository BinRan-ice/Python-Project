# coding:utf-8

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
class Demo(QWidget):
    def __init__(self,parent=None):
        super(Demo,self).__init__(parent)
        self.setWindowTitle("使用QPainter绘制图形")
        self.resize(300,120)
    def paintEvent(self,event):
        #创建绘图对象
        qp=QPainter(self)
        #设置画笔
        qp.setPen(Qt.red)
        #绘制一个椭圆
        qp.drawEllipse(80,10,50,30)
        #绘制一个矩形
        qp.drawRect(180,10,50,30)
        #绘制直线
        qp.drawLine(80,70,200,70)
        #绘制文本
        qp.drawText(90,100,"Hello PyQt5")

if __name__=="__main__":
    import sys
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec_())