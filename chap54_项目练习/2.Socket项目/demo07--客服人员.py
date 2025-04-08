# coding:utf-8
import socket

# (1)创建socket对象
recv_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# (2)绑定IP地址和端口号
recv_socket.bind(("127.0.0.1", 8888))

while True:
    # (3)接收发送过来的数据
    recv_data, addr = recv_socket.recvfrom(1024)
    print('客户说：', recv_data.decode('utf-8'))
    if recv_data.decode('utf-8') == 'bye':
        break
    # (4)准备回复对方的数据
    data = input('客服回：')
    recv_socket.sendto(data.encode('utf-8'), addr)

# (5)关闭socket对象
recv_socket.close()