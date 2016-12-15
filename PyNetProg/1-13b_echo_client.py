#!/usr/bin/python
#Python network programming cookbook -- Chapter 1.13b
import socket
import sys
import argparse

host = 'localhost'
def echo_client(port):
    """A simple echo client"""
    #Creamos el socket TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Conectar el socket al servidor
    server_address = (host,port)
    print "Connecting to %s port %s" % server_address
    sock.connect(server_address)

    #Enviar datos
    try:
        message = "Test message. This will be echoed"
        print "Sending %s" % message
        sock.sendall(message)
        #Buscar una respuesta
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print "received: %s" %data
    except socket.errno, e:
        print "socket error: %s" %str(e)
    except Exception, e:
        print "Other exception: %s" %str(e)
    finally:
        print "Closing connection to the server"
        sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket server client')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_client(port)
