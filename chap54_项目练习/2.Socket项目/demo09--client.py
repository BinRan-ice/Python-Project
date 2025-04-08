# coding:utf-8
import wx

class Client(wx.Frame):
    def __init__(self,client_name):
        #调用父类的初始化方法
        #None表示没有父级窗口
        #id表示窗口的编号
        #size表示窗口的大小
        wx.Frame.__init__(self,None,id=1001,title=client_name+"的客户端界面",pos=wx.DefaultPosition,size=(400,450))
        #创建面板
        pl=wx.Panel(self)
        #在面板中放入盒子
        box=wx.BoxSizer(wx.VERTICAL)    #垂直方向布局
        #可伸缩的网格布局
        fgz1=wx.FlexGridSizer(wx.HSCROLL)   #水平方向布局
        #创建两个按钮
        conn_btn=wx.Button(pl,size=(200,40),label="连接")
        dis_conn_btn=wx.Button(pl,size=(200,40),label="断开")
        #把两个按钮放到可伸缩的网格布局
        fgz1.Add(conn_btn,1,wx.TOP|wx.LEFT)
        fgz1.Add(dis_conn_btn,1,wx.TOP|wx.RIGHT)
        #可伸缩的网格布局放到盒子中
        box.Add(fgz1,1,wx.ALIGN_CENTRE)
        #只读文本框
        self.show_text=wx.TextCtrl(pl,size=(400,210),style=wx.TE_MULTILINE|wx.TE_READONLY)
        #把文本框放到盒子中
        box.Add(self.show_text,1,wx.ALIGN_CENTRE)
        #创建聊天内容的文本框
        self.chat_text=wx.TextCtrl(pl,size=(400,120),style=wx.TE_MULTILINE|wx.TE_READONLY)
        #把文本框放到盒子中
        box.Add(self.chat_text,1,wx.ALIGN_CENTRE)
        # 可伸缩的网格布局
        fgz2 = wx.FlexGridSizer(wx.HSCROLL)  # 水平方向布局
        # 创建两个按钮
        reset_btn = wx.Button(pl, size=(200, 40), label="重置")
        send_btn = wx.Button(pl, size=(200, 40), label="发送")
        # 把两个按钮放到可伸缩的网格布局
        fgz2.Add(reset_btn, 1, wx.TOP | wx.LEFT)
        fgz2.Add(send_btn, 1, wx.TOP | wx.RIGHT)
        # 可伸缩的网格布局放到盒子中
        box.Add(fgz2, 1, wx.ALIGN_CENTRE)
        #把盒子放到面板中
        pl.SetSizer(box)

if __name__ == '__main__':
    #初始化应用程序
    app=wx.App()
    #创建客户端对象
    client=Client("张三")
    #显示客户端界面
    client.Show()
    #启动应用程序
    app.MainLoop()

