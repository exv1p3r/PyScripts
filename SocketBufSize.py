#!/usr/bin/env python2
import socket

SND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096

def modify_buff_size():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Get the size of the socket send buffer
    bufsize = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print "[*] Buffer size [Before]: %d" %bufsize
    
    s.setsockopt(socket.SOL_TCP, socket.SO_SNDBUF)
    s.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_SNDBUF,
        SND_BUF_SIZE)
    s.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_RCVBUF,
        RECV_BUF_SIZE
    )

    bufsize = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print "[*] Buffer size [After]: %d" %bufsize

if __name__ == '__main__':
    modify_buff_size()