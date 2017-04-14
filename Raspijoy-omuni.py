from __future__ import print_function
import socket
from contextlib import closing
from motor import Ax12

self = Ax12()
self.setAngleLimit(1,0,0)
self.setAngleLimit(2,0,0)
self.setAngleLimit(3,0,0)

def main():
    host = 'soiya.local'
    port = 9112
    backlog = 10
    bufsize = 4096

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    with closing(sock):
        sock.bind((host,port))
        sock.listen(backlog)
        while True:
            conn,address = sock.accept()
            with closing(conn):
"2joyjoy.py" 46L, 1261C                                       1,1          先頭
from __future__ import print_function
import socket
from contextlib import closing
from motor import Ax12

self = Ax12()
self.setAngleLimit(1,0,0)
self.setAngleLimit(2,0,0)
self.setAngleLimit(3,0,0)

def main():
    host = 'soiya.local'
    port = 9112
    backlog = 10
    bufsize = 4096

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    with closing(sock):
        sock.bind((host,port))
        sock.listen(backlog)
        while True:
            conn,address = sock.accept()
            with closing(conn):
                msg = conn.recv(bufsize)
                sp1 = int(msg)/100000000
                sp2 =(int(msg)-(sp1*100000000))/10000
                sp3 =int(msg)-(sp1*100000000)-(sp2*10000)
                if 200<=sp1<=1023:
                        sp1 = 200
                elif 1225<=sp1<=2024:
                        sp1 = 1224
                if 200<=sp2<=1023:
                        sp2 = 200
                elif 1225<=sp2<=2024:
                        sp2 = 1224
                if 200<=sp3<=1023:
                        sp3 = 200
                elif 1225<=sp3<=2024:
                        sp3 = 1224
                print(msg)
                self.moveSpeed(2,0,int(sp2))
                self.moveSpeed(1,0,int(sp1))
                self.moveSpeed(3,0,int(sp3))
    return
if __name__ == '__main__':
    main()
