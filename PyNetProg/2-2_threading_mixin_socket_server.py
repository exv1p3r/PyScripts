#!/usr/bin/env python
#Python network programming cookbook - Chapter 2.2

import os
import socket
import threading
import SocketServer

SERVER_HOST = 'localhost'
SERVER_PORT = 0
BUF_SIZE = 1024

def client(ip, port, message):
    """A client to test threading mixin server"""
    #Connect to the server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(message)
        response = sock.recv(BUF_SIZE)
        print 'Client received: %s' %response
    finally:
        sock.close()

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    """An example of threaded TCP request handler"""
    def handle(self):
        data = self.request.recv(1024)
        current_thread = threading.current.thread()
        response = "%s: %s" % (current_thread.name, data)
        self.request.sendall(response)

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    """Nothing to add here, inherited everything necessary from parents"""
    pass

if __name__ == '__main__':
    #Correr el servidor
    server = ThreadedTCPServer((SERVER_HOST, SERVER_PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address #Recibe una direccion IP
    #Comenzar una sesion con el servidor
    server_thread = threading.Thread(target=server.serve_forever)
    #Salir del servidor
    server_thread.daemon = True
    server_thread.start()
    print "Server loop running on thread: %s" %server_thread.name
    #Correr los clientes
    client(ip, port, "Hello from client 1")
    client(ip, port, "Hello from client 2")
    client(ip, port, "Hello from client 3")
    #Limpieza del servidor
    server.shutdown()
