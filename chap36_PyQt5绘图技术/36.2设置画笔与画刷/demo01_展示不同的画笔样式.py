# coding:utf-8
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt


class Demo(QWidget):
    def __init__(self, parent=None):
        super(Demo, self).__init__(parent)
        self.setWindowTitle("展示不同的画笔样式")
        self.resize(300, 120)

    def paintEvent(self, event):
        qp = QPainter(self)  # 创建绘图对象
        pen = QPen()  # 创建画笔对象
        # 设置第一条直线画笔
        pen.setColor(Qt.red)  # 设置画笔颜色为红色
        pen.setStyle(Qt.SolidLine)  # 设置画笔样式为实线
        pen.setWidth(1)  # 设置画笔宽度为1
        qp.setPen(pen)  # 将画笔设置到绘图对象
        qp.drawLine(80, 10, 200, 10)  # 绘制直线
        # 设置第二条直线画笔
        pen.setColor(Qt.blue)  # 设置画笔颜色为蓝色
        pen.setStyle(Qt.DashLine)  # 设置画笔样式为虚线
        pen.setWidth(2)  # 设置画笔宽度为2
        qp.setPen(pen)  # 将画笔设置到绘图对象
        qp.drawLine(80, 30, 200, 30)  # 绘制直线
        # 设置第三条直线画笔
        pen.setColor(Qt.cyan)  # 设置画笔颜色为青色
        pen.setStyle(Qt.DotLine)  # 设置画笔样式为点线
        pen.setWidth(3)  # 设置画笔宽度为3
        qp.setPen(pen)  # 将画笔设置到绘图对象
        qp.drawLine(80, 50, 200, 50)  # 绘制直线
        # 设置第四条直线画笔
        pen.setColor(Qt.green)  # 设置画笔颜色为绿色
        pen.setStyle(Qt.DashDotLine)  # 设置画笔样式为点划线
        pen.setWidth(4)  # 设置画笔宽度为4
        qp.setPen(pen)  # 将画笔设置到绘图对象
        qp.drawLine(80, 70, 200, 70)  # 绘制直线
        # 设置第五条直线画笔
        pen.setColor(Qt.black)  # 设置画笔颜色为黑色
        pen.setStyle(Qt.DashDotDotLine)  # 设置画笔样式为点点划线
        pen.setWidth(5)  # 设置画笔宽度为5
        qp.setPen(pen)  # 将画笔设置到绘图对象
        qp.drawLine(80, 90, 200, 90)  # 绘制直线
        # 设置第六条直线画笔
        pen.setColor(QColor(48, 235, 100))  # 设置画笔颜色为紫色
        pen.setStyle(Qt.CustomDashLine)  # 设置画笔样式为自定义样式
        pen.setDashPattern([1, 3, 2, 3])  # 设置画笔的虚线间隔
        pen.setWidth(6)  # 设置画笔宽度为6
        qp.setPen(pen)  # 将画笔设置到绘图对象
        qp.drawLine(80, 110, 200, 110)  # 绘制直线


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
