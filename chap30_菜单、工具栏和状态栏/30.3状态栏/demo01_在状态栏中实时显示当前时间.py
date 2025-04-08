# coding:utf-8
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(301, 107)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        # 添加一个状态栏
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # 创建一个QTimer计时器对象
        timer = QtCore.QTimer(MainWindow)
        # 发射timeout信号，与自定义槽函数相关联
        timer.timeout.connect(self.showtime)
        # 启动计时器
        timer.start()

    # 自定义槽函数，用来在状态栏中显示当前时间
    def showtime(self):
        # 获取系统当前时间
        datetime = QtCore.QDateTime.currentDateTime()
        # 对日期时间进行格式化
        text = datetime.toString("yyyy-MM-dd HH:mm:ss")
        # 在状态栏中显示当前时间
        self.statusbar.showMessage("当前日期时间：" + text, 0)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()  # 创建窗口对象
    ui = Ui_MainWindow()  # 创建PyQt设计的窗体对象
    ui.setupUi(MainWindow)  # 调用PyQt窗体的方法对窗体对象进行初始化设置
    MainWindow.show()  # 显示窗体
    sys.exit(app.exec_())  # 程序关闭时退出进程
