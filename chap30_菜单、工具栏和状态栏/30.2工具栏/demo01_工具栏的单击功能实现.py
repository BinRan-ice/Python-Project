# coding:utf-8
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(309, 137)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        # 设置工具栏可移动
        self.toolBar.setMovable(True)
        # 设置工具栏为水平工具栏
        self.toolBar.setOrientation(QtCore.Qt.Horizontal)
        # 设置工具栏中按钮的显示方式为：文字显示在图标的下方
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        # 为工具栏添加QAction
        self.toolBar.addAction(QtGui.QIcon("../image/new.ico"), "新建")
        # 创建打开按钮对象
        self.open = QtWidgets.QAction(QtGui.QIcon("../image/open.ico"), "打开")
        # 创建关闭按钮对象
        self.close = QtWidgets.QAction(QtGui.QIcon("../image/close.ico"), "关闭")
        # 将创建的两个Action添加到工具栏中
        self.toolBar.addActions([self.open, self.close])
        # 设置工具栏图标按钮的大小
        self.toolBar.setIconSize(QtCore.QSize(16, 16))
        # 创建一个ComboBox下拉列表控件
        self.comboBox = QtWidgets.QComboBox()
        # 定义职位列表
        list = ["总经理", "副总经理", "人事部经理", "财务部经理", "部门经理", "普通员工"]
        # 将职位列表添加到下拉列表控件中
        self.comboBox.addItems(list)
        # 将下拉列表控件添加到工具栏中
        self.toolBar.addWidget(self.comboBox)
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        # 将ComboBox下拉列表控件的内容改变信号与槽函数进行连接
        self.comboBox.currentIndexChanged.connect(self.showinfo)
        # 为菜单中的Action绑定triggered信号
        self.toolBar.actionTriggered[QtWidgets.QAction].connect(self.getvalue)

    def getvalue(self, m):
        # 使用information()方法弹出信息提示框
        QMessageBox.information(MainWindow, "提示", "您点击了" + m.text(), QMessageBox.Ok)

    def showinfo(self):
        # 显示选择的职位
        QMessageBox.information(MainWindow, "提示", "您选择的职位是" + self.comboBox.currentText(), QMessageBox.Ok)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "工具栏"))


import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()  # 创建窗口对象
    ui = Ui_MainWindow()  # 创建PyQt设计的窗体对象
    ui.setupUi(MainWindow)  # 调用PyQt窗体的方法对窗体对象进行初始化设置
    MainWindow.show()  # 显示窗体
    sys.exit(app.exec_())  # 程序关闭时退出进程
