# coding:utf-8

from PyQt5.QtWidgets import *
from PyQt5 import QtCore

class Demo(QWidget):
    def __init__(self, parent=None):
        super(Demo, self).__init__(parent)
        # 初始化窗口
        self.initUI()

    def initUI(self):
        self.setWindowTitle("获取文件信息")
        #创建网格布局
        layout=QGridLayout()
        #创建标签
        label1=QLabel()
        label1.setText("文件路径：")
        layout.addWidget(label1,0,0,QtCore.Qt.AlignRight)
        #创建显示选中文件的文本框
        self.text1=QLineEdit()
        layout.addWidget(self.text1,0,1,1,3,QtCore.Qt.AlignLeft)
        #创建选择按钮
        button1=QPushButton()
        button1.setText("选择")
        button1.clicked.connect(self.selectFile)
        layout.addWidget(button1,0,4,QtCore.Qt.AlignLeft)
        #显示文本信息的文本浏览器
        self.text2=QTextBrowser()
        layout.addWidget(self.text2,1,0,1,5,QtCore.Qt.AlignLeft)
        #设置网格布局
        self.setLayout(layout)

    def selectFile(self):
        #创建文件对话框
        fileDialog=QFileDialog()
        #设置初始路径为从c盘开始
        fileDialog.setDirectory("C:/")
        #判断是否选择了文件
        if fileDialog.exec():
            #获取选择的文件
            filename=fileDialog.selectedFiles()[0]
            #将文件路径显示到文本框中
            self.text1.setText(filename)
            import os,time
            #获取文件信息
            info=os.stat(filename)
            self.text2.setText("文件完整路径："+os.path.abspath("filename")+"\n文件大小："+str(info.st_size)+"\n文件创建时间："+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(info.st_ctime))+"\n文件最后修改时间："+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(info.st_mtime))+"\n文件最后访问时间："+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(info.st_atime)))

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    demo=Demo()
    demo.show()
    sys.exit(app.exec_())