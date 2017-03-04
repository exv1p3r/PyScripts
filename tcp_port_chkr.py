#!/usr/bin/python2
import socket
import re
import sys

def check_srv(port, addr):
    #Create a TCP Socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Attempting to connect to %s on port %s" % (addr, port)
    try:
        s.connect((addr, port))
        print "Connected to %s on port %d" % (addr, port)
        return True
    except socket.error, e:
        print "Connection to %s on port %d failed: %s" % (addr, port, e)
        return False
if __name__ == "__main__":
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-a", "--address", dest="addr", default="localhost",
            help="Address for server", metavar="ADRESS") 
    parser.add_option("-p", "--port", dest="port", default=80, help="PORT for server",
            metavar="PORT")
    (options, args) = parser.parse_args()
    print "Options: %s , args: %s" % (options, args)
    check = check_srv(options.addr, options.port)
    print "Check server returned %s" % check
    sys.exit(not check)
