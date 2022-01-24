from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM
from socket import gethostname,gethostbyname

def start_client(port):
    sk=socket(AF_INET,SOCK_STREAM)
    host=gethostname()
    host_ip=gethostbyname(host)
    sk.connect((host,port))
    while True:
       message=input()
       sk.send(bytes(message,'utf-8'))
       rcv=sk.recv(1024).decode('utf-8')
       print(rcv)
    sk.close()

if __name__=="__main__":
   start_client(1234)
   