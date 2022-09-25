from socket import *

tcp_socket = socket(AF_INET,SOCK_STREAM)
SERVER_HOST = input('Enter ip address(127.0.0.1): ')
SERVER_PORT = int(input('Enter Port(5500): '))
tcp_socket.connect((SERVER_HOST, SERVER_PORT))
print("Enter the coefficients for the equation: ax^2 + bx + c = 0")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
tcp_socket.send(f'{a},{b},{c}'.encode())
recv_data = tcp_socket.recv(1024)
print(f'Result: \n{recv_data.decode()}')

tcp_socket.close()