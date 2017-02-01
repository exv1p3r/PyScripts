#!/usr/bin/env python2
#-*- coding: utf-8 -*-#
import paramiko

#Datos de el servidor al que nos vamos a conectar
hostname = ''
port = 2022
username = ''
password = ''

def main():
    paramiko.util.log_to_file('paramiko.log')
    s = paramiko.SSHClient()                                #Creamos el cliente SSH 
    s.load_system_host_keys()                               #Cargamos las host keys 
    s.connect(hostname, port, username, password)           #Creamos la conexión 
    stdin, stdout, stderr = s.exec_command('ifconfig')      #exec_command regresa tres "archivos" de asociación con la ejecución de este: standard input, standard output, standard error
    print stdin.read()                                      #Imprimimos el resultado de la entrada standard (stdin)
    s.close()                                               #Cerramos la conexión

if __name__ == '__main__':
    main()