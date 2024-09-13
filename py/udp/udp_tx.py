import time
import datetime
from socket import socket, AF_INET, SOCK_DGRAM

DEF_ADDR = "127.0.0.1"   # localhost
DEF_PORT = 1234


def main_test():
    sock = socket(AF_INET, SOCK_DGRAM)
    i:int = 0
    while True :
        pd_bytes = b'\x00\x7E\x55\x12' 
        udp_str = format(i, '06d') + ":" + format(int.from_bytes(pd_bytes, "big"), '08X')
        print(udp_str)
        sock.sendto(bytes(udp_str, 'utf-8'), (DEF_ADDR, DEF_PORT))
        i += 1
        time.sleep(0.5)


if __name__ == "__main__":
    main_test()

