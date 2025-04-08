# coding:utf-8
from socket import socket,AF_INET,SOCK_STREAM
#AF_INET表示使用IPv4协议,SOCK_STREAM表示使用TCP协议

#(1)创建socket对象
server_socket = socket(AF_INET,SOCK_STREAM)

#(2)绑定IP地址和端口号
ip='127.0.0.1'  #本地回环地址
port=8888    #端口号
server_socket.bind((ip,port))

#(3)使用listen()方法监听端口
server_socket.listen(5)  #最大连接数为5
print('服务器启动成功，等待客户端连接...')

#(4)等待客户端连接
client_socket,client_addr=server_socket.accept()  #accept()方法返回一个元组，元组中包含两个元素，第一个元素是客户端的socket对象，第二个元素是客户端的地址和端口号

#(5)接收客户端发送的数据
data=client_socket.recv(1024)  #recv()方法接收数据，参数表示一次接收的最大字节数
print('接收到客户端的数据：',data.decode('utf-8'))    #y要求接收到的数据是utf-8编码格式

#(6)关闭socket对象
client_socket.close()