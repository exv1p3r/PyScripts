#!/usr/bin/env python
#Python network programming cookbook -- chapter 1

import socket

def print_machine_info():
    #Funcion gethostname() sirve para obtener el nombre del host
    host_name = socket.gethostname()
    #Funcion gethostbyname() sirve para obtener la dirección IP del host
    ip_add = socket.gethostbyname(host_name)
    print "Hostname : %s" % host_name
    print "IP address: %s" % ip_add
if __name__ == '__main__':
    print_machine_info()
