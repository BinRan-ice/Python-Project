# coding:utf-8
import socket

#(1)创建socket对象
socket_obj= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#(2)绑定IP地址和端口号
ip='127.0.0.1'  #本地回环地址
port=8888    #端口号
socket_obj.bind((ip,port))

#(3)使用listen()方法监听端口
socket_obj.listen(5)  #最大连接数为5
print('服务器启动成功，等待客户端连接...')

#(4)等待客户端连接
client_socket,client_addr=socket_obj.accept()  #accept()方法返回一个元组，元组中包含两个元素，第一个元素是客户端的socket对象，第二个元素是客户端的地址和端口号
print('客户端地址和端口号：',client_addr)

#(5)接收客户端发送的数据
info=client_socket.recv(1024).decode('utf-8')  #recv()方法接收数据，参数表示一次接收的最大字节数
while info!='bye':
    if info!='':
        print('接收到客户端的数据：',info)
    #准备发送数据
    data=input('请输入要发送的数据：')
    #服务端回复客户端的信息
    client_socket.send(data.encode('utf-8'))
    if data=='bye':
        break
    info=client_socket.recv(1024).decode('utf-8')

#(6)关闭socket对象
client_socket.close()
socket_obj.close()