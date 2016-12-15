#!/usr/bin/env python
#Python network programming cookbook - chapter 1.6

import socket

def socket_timeout():
    #Se define la variable s como un socket del protocolo INET de la familia STREAM 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Default socket timeout: %s" %s.gettimeout()
    s.settimeout(100)
    print "Current socket timeout: %s" %s.gettimeout()

if __name__ == '__main__':
    socket_timeout()
