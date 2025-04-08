# coding:utf-8
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import random

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(435, 294)
        MainWindow.setWindowTitle("双色球彩票选号器")
        # 设置窗口背景图片
        MainWindow.setStyleSheet("border-image:url(../image/双色球彩票选号器.jpg);")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        # 创建第一个红球数字的标签
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(97, 178, 31, 31))
        # 设置标签的字体
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        # 设置标签的文字颜色
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        # 创建第二个红球数字的标签
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(153, 179, 31, 31))
        self.label_2.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        # 创建第三个红球数字的标签
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(209, 179, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        # 创建第四个红球数字的标签
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(269, 179, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        # 创建第五个红球数字的标签
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(325, 179, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        # 创建第六个红球数字的标签
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        self.label_6.setGeometry(QtCore.QRect(380, 180, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        # 创建第一个蓝球数字的标签
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        self.label_7.setGeometry(QtCore.QRect(96, 241, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        #创建开始按钮
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(310,235,51,51))
        # 设置按钮的背景图片
        self.pushButton.setStyleSheet("border-image:url(../image/开始.jpg);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        # 创建停止按钮
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 235, 51, 51))
        self.pushButton_2.setStyleSheet("border-image:url(../image/停止.jpg);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralWidget)
        #初始化显示双色球数字的Label标签的默认文本
        self.label.setText("00")
        self.label_2.setText("00")
        self.label_3.setText("00")
        self.label_4.setText("00")
        self.label_5.setText("00")
        self.label_6.setText("00")
        self.label_7.setText("00")
        #设置显示双色球数字的label标签背景透明
        self.label.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label_2.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label_3.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label_4.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label_5.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label_6.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label_7.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #设置开始按钮的单击信号与槽函数的连接
        self.pushButton.clicked.connect(self.start)
        #设置停止按钮的单击信号与槽函数的连接
        self.pushButton_2.clicked.connect(self.stop)

    #定义槽函数，用来开始计时器
    def start(self):
        #创建计时器对象
        self.timer = QTimer(MainWindow)
        #开始计时器
        self.timer.start()
        #设置计时器要执行的槽函数
        self.timer.timeout.connect(self.num)

    #定义槽函数，用来设置七个label标签的文本
    def num(self):
        #随机生成第一个红球数字
        self.label.setText("{0:02d}".format(random.randint(1,33)))
        #随机生成第二个红球数字
        self.label_2.setText("{0:02d}".format(random.randint(1,33)))
        #随机生成第三个红球数字
        self.label_3.setText("{0:02d}".format(random.randint(1,33)))
        #随机生成第四个红球数字
        self.label_4.setText("{0:02d}".format(random.randint(1,33)))
        #随机生成第五个红球数字
        self.label_5.setText("{0:02d}".format(random.randint(1,33)))
        #随机生成第六个红球数字
        self.label_6.setText("{0:02d}".format(random.randint(1,33)))
        #随机生成蓝球数字
        self.label_7.setText("{0:02d}".format(random.randint(1,16)))

    #定义槽函数，用来停止计时器
    def stop(self):
        #停止计时器
        self.timer.stop()

import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()  # 创建窗口对象
    ui = Ui_MainWindow()  # 创建PyQt设计的窗体对象
    ui.setupUi(MainWindow)  # 调用PyQt窗体的方法对窗体对象进行初始化设置
    MainWindow.show()  # 显示窗体
    sys.exit(app.exec_())  # 程序关闭时退出进程
