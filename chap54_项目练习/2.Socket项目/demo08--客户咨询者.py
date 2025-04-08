# coding:utf-8
import socket

#(1)创建socket对象
send_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    #(2)准备发送数据
    data = input('客户说：')

    #(3)发送数据
    send_socket.sendto(data.encode('utf-8'),('127.0.0.1',8888))
    if data == 'bye':
        break

    #(4)接收来自客服回复的数据
    recv_data,addr = send_socket.recvfrom(1024)
    print('客服说：',recv_data.decode('utf-8'))

#(5)关闭socket对象
send_socket.close()