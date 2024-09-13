from socket import socket, AF_INET, SOCK_DGRAM

HOST = ""
PORT = 1234

s = socket(AF_INET, SOCK_DGRAM)
s.bind((HOST, PORT))

while True:
    try:
        data, address = s.recvfrom(65535)
        print(f"data:{data},from:{address}")
    except KeyboardInterrupt:
        print("Exit")
        s.close()
