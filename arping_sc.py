#!/usr/bin/env python2
from scapy.all import srp,Ether,ARP,conf
import sys

def arping(iprange='192.168.30.0/24'):
    """ARPING function takes IP address or network, returns nested mac/ip list"""

    conf.verb=0
    ans,unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=iprange), timeout=2)

    collection = []
    for snd, rcv in ans:
        result = rcv.sprintf(r"%ARP.psrc% %Ether.src%").split()
        collection.append(result)
    return collection

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for ip in sys.argv[1:]:
            print "arping", ip
            print arping(ip)
    else:
        print arping()