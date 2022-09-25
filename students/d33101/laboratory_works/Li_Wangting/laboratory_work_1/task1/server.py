import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("127.0.0.1", 5500))
 
while True:
    data, addr = s.recvfrom(1024)
    print(f"Client: {data.decode()}\n")
    if data == b"exit":
        s.sendto(b"Bye!", addr)
        break
    elif data == b"Hello, server":
        s.sendto(b"Hello, client", addr)
    else:
        s.sendto(b"Bip-boop-biiip", addr)
s.close()