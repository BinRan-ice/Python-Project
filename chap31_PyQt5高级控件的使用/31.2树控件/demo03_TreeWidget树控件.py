# coding:utf-8
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTreeWidgetItem


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 210)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(0, 0, 300, 210))
        self.treeWidget.setObjectName("treeWidget")
        # 设置树结构中的列数
        self.treeWidget.setColumnCount(2)
        # 设置列标题名
        self.treeWidget.setHeaderLabels(['姓名', '职务'])
        # 创建结点
        root = QTreeWidgetItem(self.treeWidget)
        # 设置顶级结点的文本
        root.setText(0, '结构组织')
        # 定义字典，，存储树中显示的数据
        dict = {'任正非': '华为董事长', '李彦宏': '百度 CEO', '马化腾': '腾讯 CEO', '马云': '阿里巴巴创始人',
                '董明珠': '格力电器董事长'}
        # 遍历字典
        for key, value in dict.items():
            # 创建子结点
            child = QTreeWidgetItem(root)
            # 为子节点设置图标
            if key == '任正非':
                child.setIcon(0, QtGui.QIcon('../image/华为.jpg'))
            elif key == '李彦宏':
                child.setIcon(0, QtGui.QIcon('../image/百度.jpg'))
            elif key == '马化腾':
                child.setIcon(0, QtGui.QIcon('../image/腾讯.png'))
            elif key == '马云':
                child.setIcon(0, QtGui.QIcon('../image/阿里巴巴.jpg'))
            elif key == '董明珠':
                child.setIcon(0, QtGui.QIcon('../image/格力.jpeg'))
            # 设置子结点的文本
            child.setText(0, key)
            child.setText(1, value)
            # 为结点设置复选框，并且选中
            child.setCheckState(0, QtCore.Qt.Checked)
        # 将创建的树节点添加到树控件中
        self.treeWidget.addTopLevelItem(root)
        # 展开所有树节点
        self.treeWidget.expandAll()
        # 设置隔行变色
        self.treeWidget.setAlternatingRowColors(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 为树控件的单击事件绑定槽函数
        self.treeWidget.clicked.connect(self.showText)

    # 显示单击的树节点的文本
    def showText(self, index):
        # 获取当前选中项
        item = self.treeWidget.currentItem()
        # 弹出提示框，显示选中项的文本
        QtWidgets.QMessageBox.information(MainWindow, '提示', '您选择的是：{0}--{1}'.format(item.text(0), item.text(1)),
                                          QtWidgets.QMessageBox.Ok)

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
