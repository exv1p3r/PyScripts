#!/usr/bin/python
#Python network programming cookbook - Chapter 2.1

import os
import socket
import threading
import SocketServer

SERVER_HOST = 'localhost'
SERVER_PORT = 0 #Le dice al kernel que tome un puerto automaticamente
BUF_SIZE = 1024
ECHO_MSG = 'Hello echo server!!'

class ForkedClient():
    """A client to test forking server"""
    def __init__(self, ip, port):
        #Creamos el socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #Conectamos al servidor
        self.sock.connect((ip, port))

    def run(self):
        """Client playing with the server"""
        #Enviar los datos al servidor
        current_process_id = os.getpid()
        print 'PID %s Sending echo message to the server: "%s"' %(current_process_id, ECHO_MSG)
        sent_data_length = self.sock.send(ECHO_MSG)
        print "Sent: %d characters, so far..." % sent_data_length

        #Mostrar la respuesta del servidor
        response = self.sock.recv(BUF_SIZE)
        print "PID %s received: %s" % (current_process_id, response[5:])

    def shutdown(self):
        """Cleanup the client socket"""
        self.sock.close()

class ForkingServerRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        #Enviar el echo de regreso al server
        data = self.request.recv(BUF_SIZE)
        current_process_id = os.getpid()
        response = '%s: %s' % (current_process_id, data)
        print "Server sending response [current_process_id: data] = [%s]" %response
        self.request.send(response)
        return

class ForkingServer(SocketServer.ForkingMixIn, SocketServer.TCPServer):
    """Nothing to add here
    Inherited everything necessary from parents"""
    pass

def main():
    #Iniciar el Server
    server = ForkingServer((SERVER_HOST, SERVER_PORT), ForkingServerRequestHandler)
    ip, port = server.server_address #Obtiene el numero del puerto
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.setDaemon(True) #No se "cuelga" al salir
    server_thread.start()
    print 'Server loop running PID: %s' %os.getpid()

    #Lanzar el cliente(s)
    client1 = ForkedClient(ip, port)
    client1.run()

    client2 = ForkedClient(ip, port)
    client2.run()

    #Clean them up
    server.shutdown()
    client1.shutdown()
    client2.shutdown()
    server.socket.close()

if __name__ == '__main__':
    main()
