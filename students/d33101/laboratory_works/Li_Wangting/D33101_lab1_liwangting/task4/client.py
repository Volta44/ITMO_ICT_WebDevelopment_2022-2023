import socket
import threading

nickname = input("Nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5500))
print('Connection to server...')

def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            if message == 'NICK':
                client.send(nickname.encode())
            else:
                print(message)
        except:
            break
        
def write():
    while True:
        message = input('')
        if message == 'exit':
            print('Break connetion...')
            client.close()
            break
        client.send(message.encode())

receive_thread = threading.Thread(target = receive)
receive_thread.start()

write_thread = threading.Thread(target = write)
write_thread.start()