# coding:utf-8
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self,MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(422, 197)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #创建一个TreeView树视图
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(0,0,421,201))
        self.treeView.setObjectName("treeView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #创建数据模型
        model=QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels(["年级","班级","姓名","分数"])
        #姓名列表
        name=["张三","李四","王五","赵六","孙七","周八","吴九","郑十","钱十一","孔十二"]
        #分数列表
        score=[80,90,70,60,50,40,30,20,10,0]
        import random
        #设置数据
        for i in range(0,6):
            #一级结点：年级，只设第一列的数据
            grade=QtGui.QStandardItem("年级%d"%(i+1))
            #一级节点
            model.appendRow(grade)
            for j in range(0,4):
                #二级结点：班级，姓名，分数
                itemClass=QtGui.QStandardItem("班级%d"%(j+1))
                itemName=QtGui.QStandardItem(name[random.randint(0,9)])
                itemScore=QtGui.QStandardItem(str(score[random.randint(0,9)]))
                #将二级节点添加到一级节点上
                grade.appendRow([QtGui.QStandardItem(""),itemClass,itemName,itemScore])
        #为树视图设置数据模型
        self.treeView.setModel(model)

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