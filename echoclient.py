# Modified Echo Client
import socket
from tools import *

def main():


    HOST = 'localhost'
    PORT = 50007
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        data = b'Hello, world'
        print('send %d bytes to server' % (len(data)))
        hexdump(data)
        data = s.recv(1024)
        print('received %d bytes from serve' % (len(data)))
        hexdump(data)
        print('Received data:', data)

if __name__== "__main__":
  main()
