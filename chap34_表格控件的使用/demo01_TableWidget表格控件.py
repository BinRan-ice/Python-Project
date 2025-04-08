# coding:utf-8
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        # 初始化窗口
        self.initUI()

    def initUI(self):
        self.setWindowTitle("使用表格显示数据库中的数据")
        # 设置窗口大小
        self.resize(450, 250)
        # 创建水平布局
        layout = QHBoxLayout()
        # 创建表格控件
        table = QTableWidget()
        import pymysql
        # 连接数据库
        db = pymysql.connect(host="192.168.154.128", user="root", passwd="root123456", database="python数据库",
                             port=3309)
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 执行sql语句
        cursor.execute("select * from books")
        # 获取所有记录列表
        results = cursor.fetchall()
        # 设置表格的行数和列数
        row = cursor.rowcount
        column = len(results[0])
        # 关闭游标连接
        cursor.close()
        # 关闭数据库连接
        db.close()
        # 设置表格的行数和列数
        table.setRowCount(row)
        table.setColumnCount(column)
        # 设置表格的标题名称
        table.setHorizontalHeaderLabels(["编号", "图书书名", "图书类别", "图书价格", "出版时间"])
        # 遍历行
        for i in range(row):
            # 遍历列
            for j in range(column):
                #将第二列设置为ComboBox下拉列表
                if j == 2:
                    # 创建下拉列表
                    combo = QComboBox()
                    # 设置下拉列表的选项
                    combo.addItems(["python", "java", "大数据", "人工智能", "云计算"])
                    # 设置下拉列表的默认选项
                    combo.setCurrentIndex(0)
                    # 将下拉列表添加到表格中
                    table.setCellWidget(i, 2, combo)
                else:
                    # 转换后可插入表格
                    data = QTableWidgetItem(str(results[i][j]))
                    table.setItem(i, j, data)
                    # 如果是第四列则显示图片
                if j == 4:
                    # 设置单元格的图片
                    data = QTableWidgetItem(QtGui.QIcon("image/date.png"), str(results[i][j]))
                else:
                    # 转换后可插入表格
                    data = QTableWidgetItem(str(results[i][j]))
                # 设置单元格的文本颜色
                data.setForeground(QtGui.QBrush(QtGui.QColor("green")))
                # 设置单元格的背景颜色
                data.setBackground(QtGui.QBrush(QtGui.QColor("yellow")))
                # 如果是第四列则显示图片

                table.setItem(i, j, data)
        # 使列宽跟随内容变化
        table.resizeColumnsToContents()
        # 使行高跟随内容变化
        table.resizeRowsToContents()
        # 使表格颜色交替显示
        table.setAlternatingRowColors(True)
        # 隐藏垂直标
        table.verticalHeader().setVisible(False)
        # 设置最后一列自动填充容器
        table.horizontalHeader().setStretchLastSection(True)
        # 禁止编辑单元格
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 设置降序排序
        table.sortItems(4, QtCore.Qt.DescendingOrder)
        # 将表格添加到水平布局中
        layout.addWidget(table)
        # 设置当前窗口的布局方式
        self.setLayout(layout)


import sys

if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    demo = Demo()
    # 显示窗口
    demo.show()
    # 应用程序的消息循环
    sys.exit(app.exec_())
