#!/usr/bin/env python
from scapy.all import *


HOST =[]
"""
Deteccion de los host de una red
"""
def fnd_pkts(pkg):
    if IP in pkg:
        if not pkg[IP].src in HOST:
            HOST.append(pkg[IP].src)

def main():
    print "[*] Iniciando el sniffer"
    sniff(filter='tcp in port 80', prn=fnd_pkts)    
    print "[*] Finalizando el scan"
    print "[*] Host descubiertos:"
    for x in HOST:
        print "     - %s" % x
if __name__ == '__main__':
    main()