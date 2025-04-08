# coding:utf-8

from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self,MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500,300)
        MainWindow.setWindowTitle("遍历文件夹")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #添加表格
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0,40,501,270))
        self.tableWidget.setObjectName("tableWidget")
        #设置列数
        self.tableWidget.setColumnCount(2)
        #设置第一列的标题
        item=QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0,item)
        item=self.tableWidget.horizontalHeaderItem(0)
        item.setText("文件名")
        #设置第二列的标题
        item=QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1,item)
        item=self.tableWidget.horizontalHeaderItem(1)
        item.setText("详细信息")
        #设置第一列的宽度
        self.tableWidget.setColumnWidth(0,100)
        #设置最后一列自动填充容器
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        #创建选择路径按钮
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10,10,75,23))
        #为按钮设置字体
        font=QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("选择路径")
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #为按钮的clicked信号绑定槽函数
        self.pushButton.clicked.connect(self.openDir)

    #选择路径，病落去其中的所有文件信息，将其显示在表格中
    def openDir(self):
        try:
            import os
            #dir_path为选择的文件夹的绝对路径，第二形参为对话框标题,第三形参为默认路径
            self.dir_path=QFileDialog.getExistingDirectory(None,"选择路径",os.getcwd())
            if self.dir_path != "":
                #列出文件夹下所有的目录与文件
                self.list=os.listdir(self.dir_path)
                #标识插入新行的位置
                flag=0
                #遍历文件列表
                for i in range(0,len(self.list)):
                    #拼接路径和文件名
                    path=os.path.join(self.dir_path,self.list[i])
                    #添加新行
                    self.tableWidget.insertRow(flag)
                    #设置第一列的值为文件夹(名)
                    self.tableWidget.setItem(flag,0,QtWidgets.QTableWidgetItem(self.list[i]))
                    #设置第二列的值为文件夹(路径)
                    self.tableWidget.setItem(flag,1,QtWidgets.QTableWidgetItem(path))
                    #计算下一个插入的位置
                    flag+=1
        except Exception as e:
            print(e)

if __name__ == "__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
