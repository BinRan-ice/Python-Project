# coding:utf-8
from PyQt5 import QtCore,QtGui,QtWidgets

class Ui_MainWindow(object):
    def setupUi(self,MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400,227)
        self.centralwidget=QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loading=QtWidgets.QLabel(self.centralwidget)
        self.loading.setGeometry(QtCore.QRect(150,20,100,100))
        self.loading.setStyleSheet("")
        self.loading.setText("")
        self.loading.setObjectName('loading')
        self.pushButton_start=QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(50,140,100,50))
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_stop=QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stop.setGeometry(QtCore.QRect(250,140,100,50))
        self.pushButton_stop.setObjectName("pushButton_stop")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #启动加载提示框
        self.pushButton_start.clicked.connect(self.start_loading)
        #停止加载提示框
        self.pushButton_stop.clicked.connect(self.stop_loading)

    def start_loading(self):
        #加载gif图片
        self.gif=QtGui.QMovie('../image/loading.gif')
        #设置gif图片
        self.loading.setMovie(self.gif)
        #启动gif图片，实现等待gif图片的显示
        self.gif.start()

    def stop_loading(self):
        self.gif.stop()
        self.loading.clear()

    def retranslateUi(self,MainWindow):
        _translate=QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow","MainWindow"))
        self.pushButton_start.setText(_translate("MainWindow","启动等待显示"))
        self.pushButton_stop.setText(_translate("MainWindow","停止等待现实"))

import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()  # 创建窗口对象
    ui = Ui_MainWindow()  # 创建PyQt设计的窗体对象
    ui.setupUi(MainWindow)  # 调用PyQt窗体的方法对窗体对象进行初始化设置
    MainWindow.show()  # 显示窗体
    sys.exit(app.exec_())  # 程序关闭时退出进程