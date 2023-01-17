import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 5500))
server.listen()

clients = []
nicknames = []

def broadcast(message, nickname = 'Server', client_ignore = ''):
    for client in clients:
        if client != client_ignore:
            client.send(f'{nickname}: {message.decode()}'.encode())
        
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, nicknames[clients.index(client)], client)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'<--{nickname} left!-->'.encode())
            print(f'{nickname} left!')
            nicknames.remove(nickname)
            break
        
def receive():
    while True:
        client, addr = server.accept()
        print("Connected with {}".format(str(addr)))

        client.send('NICK'.encode())
        nickname = client.recv(1024).decode()
        nicknames.append(nickname)
        clients.append(client)

        print("Nickname is {}".format(nickname))
        client.send('Connected to server!\n'.encode())
        broadcast(f"<--{nickname} joined!-->".encode())
        
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()