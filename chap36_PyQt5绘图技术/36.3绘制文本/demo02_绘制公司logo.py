# coding:utf-8
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QPixmap


class Demo(QWidget):
    def __init__(self, parent=None):
        super(Demo, self).__init__(parent)
        # 设置窗口标题
        self.setWindowTitle("绘制公司logo")
        # 设置窗口大小
        self.resize(300, 120)

    def paintEvent(self, event):
        # 创建绘图对象
        painter = QPainter(self)
        # 默认大小
        painter.drawPixmap(10, 10, QPixmap("../image/logo.jpg"))
        # 指定大小
        painter.drawPixmap(10, 10, 290, 110, QPixmap("../image/logo.jpg"))


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
