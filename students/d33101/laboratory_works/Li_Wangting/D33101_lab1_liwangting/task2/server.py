import socket
import math

def Quadratic(a, b, c):
    discr = b ** 2 - 4 * a * c
    
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        return(f'x1 = {x1}\nx2 = {x2}')
    elif discr == 0:
        x = -b / (2 * a)
        return(f"x = {x}")
    else:
        return("No solution")

tcp_socket_host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket_host.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
tcp_socket_host.bind(('127.0.0.1', 5500))
tcp_socket_host.listen()

while True:
    conn,addr = tcp_socket_host.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            data = [float(num) for num in data.decode().split(',')]
            conn.send(str(Quadratic(data[0], data[1], data[2])).encode())
