# coding:utf-8
from PyQt5.QtCore import QThread
class Thread(QThread):
    def __init__(self, parent=None):
        super(Thread, self).__init__(parent)
    #重写run()方法
    def run(self):
        #定义一个变量，用来叠加输出
        num=0
        #定义无限循环
        while True:
            #变量叠加
            num+=1
            #输出变量
            print(num)
            #使线程休眠1秒
            Thread.sleep(1)
            #如果数字到10
            if num==10:
                #退出线程
                Thread.quit()

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    #创建线程对象
    thread = Thread()
    #启动线程
    thread.start()
    sys.exit(app.exec_())