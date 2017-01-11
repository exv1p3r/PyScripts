#!/usr/bin/python2

from Scapy.all import IP, ICMP, send, RandIP, RandShort, RandByte

def random_bool():
    """Devuelve un valor booleano de manera aleatoria"""
    return int(RandInt()) % 2


def main():
    print "[*] Starting fuzzing"
    for i in range(5):

        #Fuzz IP layer
        ip_layer = IP(dst='192.168.30.254', src=RandIP(), id=RandShort())
        #Fuzz ICMP layer
        icmp_layer = ICMP(type=RandByte(), seq=RandInt())




        pkg = ip_layer/icmp_layer
        send(pkg)
if __name__ == 'main':
    main()
