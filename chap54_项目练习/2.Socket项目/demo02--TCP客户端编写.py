# coding:utf-8
import socket

#(1)创建socket对象
client_socket = socket.socket()

#(2)IP地址和端口号
ip = '127.0.0.1'
port = 8888
client_socket.connect((ip,port))
print('连接服务器成功')

#(3)发送数据
data = 'hello,服务器'
client_socket.send(data.encode('utf-8'))  #要求发送的数据是utf-8编码格式
print('发送数据成功')

#(4)关闭socket对象
client_socket.close()
print('发送完毕')