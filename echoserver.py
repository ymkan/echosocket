# Modified Echo Server
import socket
from tools import *

def main():
    HOST = ''                  # all hosts
    PORT = 50007
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            print('connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data: break
                print('received %d bytes from %s' % (len(data), str(addr)))
                hexdump(data)
                print('send %d bytes to %s' % (len(data), str(addr)))
                hexdump(data)
                conn.sendall(data)
            conn.shutdown(socket.SHUT_RDWR)
            conn.close()

if __name__== "__main__":
    main()
