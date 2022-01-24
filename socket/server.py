from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM
from threading import Thread
from socket import gethostname,gethostbyname

def create_server(host,port,handle):
    sk=socket(AF_INET,SOCK_STREAM)
    sk.bind((host,port))
    sk.listen(5)
    while True:
       conn,addr=sk.accept()
       print("Connection accepted")
       th=Thread(target=handle,args=(conn,))
       th.start()
    sk.close()

def handle(conn):
    print("Client thread created")
    while True:
        msg=conn.recv(1024).decode('utf-8')
        print(msg)
        conn.send(bytes(msg,'utf-8'))
    conn.close()

if __name__=="__main__":
   host_name=gethostname()
   host_ip=gethostbyname(host_name)
   create_server(host_ip,1234,handle)



       
      
       