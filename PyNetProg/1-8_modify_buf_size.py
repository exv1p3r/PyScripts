#!/usr/bin/env python
#Python network programming cookbook - Chapter 1.8

import socket

SND_BUF_SIZE = 4096
RCV_BUF_SIZE = 4096

def modify_buff_size():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Obtener el tamano del buffer en el socket
    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print 'Buffer size [before]: %d' %bufsize

    sock.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
    sock.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_SNDBUF,
        SND_BUF_SIZE)
    sock.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_SNDBUF,
        RCV_BUF_SIZE)
    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print "Buffer size [After]: %d" %bufsize
if __name__ == '__main__':
    modify_buff_size()
