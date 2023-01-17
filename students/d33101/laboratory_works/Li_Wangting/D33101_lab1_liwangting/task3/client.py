from socket import *

tcp_socket = socket(AF_INET,SOCK_STREAM)
tcp_socket.connect(('127.0.0.1', 5500))

tcp_socket.send('Get address'.encode())
http_adress = tcp_socket.recv(1024)
print(http_adress.decode())

tcp_socket.close()