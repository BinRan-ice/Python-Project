# coding:utf-8
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QFont
from PyQt5.QtCore import Qt
import sys, random


class Demo(QWidget):
    def __init__(self, parent=None):
        super(Demo, self).__init__(parent)
        self.setWindowTitle('绘制带噪点和干扰线的验证码')
        self.resize(150, 60)

    # 定义存储数字，字母的列表，用来从中生成验证码
    char = []
    # 添加0-9的数字
    for i in range(48, 58):
        char.append(chr(i))
    # 添加A-Z的字母
    for i in range(65, 91):
        char.append(chr(i))
    # 添加a-z的字母
    for i in range(97, 123):
        char.append(chr(i))

    # 生成随机数字或字母
    def rndChar(self):
        return self.char[random.randint(0, len((self.char)))]

    def paintEvent(self, event):
        # 创建绘图对象
        painter = QPainter(self)
        painter.drawRect(10, 10, 100, 30)
        painter.setPen(Qt.red)
        # 绘制干扰线
        for i in range(20):
            painter.drawLine(
                random.randint(10, 110), random.randint(10, 40),
                random.randint(10, 110), random.randint(10, 40)
            )
        painter.setPen(Qt.green)
        # 绘制噪声点(此处绘制500个噪声点，可以随意设置)
        for i in range(500):
            painter.drawPoint(
                random.randint(10, 110), random.randint(10, 40)
            )
        # 设置画笔
        painter.setPen(Qt.black)
        # 创建字体对象
        font = QFont()
        # 设置字体
        font.setFamily('楷体')
        # 设置字体大小
        font.setPointSize(15)
        # 设置字体加粗
        font.setBold(True)
        # 设置下划线
        font.setUnderline(True)
        painter.setFont(font)
        # 绘制文字
        for i in range(4):
            painter.drawText(30 * i + 10, 30, str(self.rndChar()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
