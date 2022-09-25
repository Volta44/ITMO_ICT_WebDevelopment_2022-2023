import socket
 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = ('127.0.0.1', 5500)
 
while True:
    msg = input("Message: ")
    if not msg: continue
    s.sendto(msg.encode(), server)
    res, server = s.recvfrom(1024)
    print(f'Server: {res.decode()}\n')
    if msg == "exit":
        print(f"Session is over...")
        break
s.close()