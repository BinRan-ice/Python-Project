# coding:utf-8
import wx
import socket

class Server(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,id=1002,title="BinRan服务器端界面",pos=wx.DefaultPosition,size=(400,450))
        #创建面板
        pl=wx.Panel(self)
        #在面板中放入盒子
        box=wx.BoxSizer(wx.VERTICAL) #垂直方向布局
        #可伸缩的网格布局
        fgz1=wx.FlexGridSizer(wx.HSCROLL)   #水平方向布局
        #创建按钮
        start_server_btn=wx.Button(pl,size=(133,40),label="启动服务")
        record_btn=wx.Button(pl,size=(133,40),label="保存聊天记录")
        stop_server_btn=wx.Button(pl,size=(133,40),label="停止服务")
        #把按钮放到可伸缩的网格布局
        fgz1.Add(start_server_btn,1,wx.TOP)
        fgz1.Add(record_btn,1,wx.TOP)
        fgz1.Add(stop_server_btn,1,wx.TOP)
        #可伸缩的网格布局放到盒子中
        box.Add(fgz1,1,wx.ALIGN_CENTRE)
        #只读多行文本框
        self.show_text = wx.TextCtrl(pl, size=(400, 410), style=wx.TE_MULTILINE | wx.TE_READONLY)
        # 把文本框放到盒子中
        box.Add(self.show_text, 1, wx.ALIGN_CENTRE)
        #把盒子放到面板中
        pl.SetSizer(box)
        """----------------------以上代码都是界面的绘制代码----------------------"""
        """----------------------以下代码是服务器功能实现的必要属性----------------------"""
        self.isOn=False    #服务器是否启动的标志
        #服务器端绑定的IP地址和端口号
        self.host_port=('',8888)
        #创建socket对象
        self.server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #绑定IP地址和端口号
        self.server_socket.bind(self.host_port)
        #设置最大连接数
        self.server_socket.listen(5)
        #创建一个字典，存储与客户端对话的会话线程
        self.session_thread_dict={}   #key:客户端名称，value:会话线程
        #当鼠标点击"启动服务"按钮时，要执行的操作
        self.Bind(wx.EVT_BUTTON,self.start_server,start_server_btn)

    def start_server(self,event):
        print("服务器启动成功！")

if __name__ == '__main__':
    #初始化应用程序
    app=wx.App()
    #创建服务器对象
    server=Server()
    #显示服务器界面
    server.Show()
    #启动应用程序
    app.MainLoop()