#!/usr/bin/env python
#Python network programming cookbook -- chapter 1.2

import socket
def get_remote_hostname():
    remote_host = 'eXv1p3r.no-ip.org'
    try:
        print "IP address: %s " %socket.gethostbyname(remote_host)
    except socket.error, err_msg:
        print "%s: %s" %(remote_host, err_msg)

if __name__ == '__main__':
    get_remote_hostname()
