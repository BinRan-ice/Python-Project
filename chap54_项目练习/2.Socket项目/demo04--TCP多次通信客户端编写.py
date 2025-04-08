# coding:utf-8
import socket

#(1)创建socket对象
client_socket = socket.socket()

#(2)IP地址和端口号
ip = '127.0.0.1'
port = 8888
client_socket.connect((ip,port))
print('连接服务器成功')

#(3)客户端发送数据
info=''
while info!='bye':
    #准备发送数据
    data=input('请输入要发送的数据：')
    #客户端发送数据
    client_socket.send(data.encode('utf-8'))
    if data=='bye':
        break
    #接收服务端回复的信息
    info=client_socket.recv(1024).decode('utf-8')
    print('接收到服务端的数据：',info)

#(4)关闭socket对象
client_socket.close()