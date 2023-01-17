import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('127.0.0.1', 5500))
server_socket.listen()
print(f"Server up and listening on port {5500}...")

while True:
    client_connection, client_address = server_socket.accept()

    with client_connection:
        request = client_connection.recv(1024).decode()
        
        file_html = open('index.html')
        response = 'HTTP/1.0 200 OK\n\n' + file_html.read()
        file_html.close()

        if request == 'Get address':
            client_connection.send(f'Address: http://127.0.0.1:5500'.encode())
        else:
            client_connection.sendall(response.encode())
        client_connection.close()
        
server_socket.close()