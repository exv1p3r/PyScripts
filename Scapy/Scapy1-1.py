#!/usr/bin/env python2

#Importamos las funciones que queremos usar de Scapy
from scapy.all import sniff

def main():
    print "Ejecutando el sniffer"
    a = sniff('tcp and port 80')
    print "Sniffer parado"
    print a

if __name__ == '__main__':
    main()
