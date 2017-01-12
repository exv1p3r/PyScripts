#!/usr/bin/env python2
#-*- coding: utf-8 -*-#
import threading
from scapy.all import IP, TCP, sr1

CONCURRENCY = 5
OPEN_PORTS = []

def analyze_port(host, port, sem):
    res = sr1(IP(dst=host)/TCP(dport=port), verbose=False, timeout=0.2)
    if res[TCP].flags == 18:
        OPEN_PORTS.append(port)
        print "Puerto %s abierto" % port
    #Desbloqueamos el semaforo para activar otro hilo
    sem.release()

def main():
    sem = threading.BoundedSemaphore(value=CONCURRENCY)
    threads = []
    #Analizamos 80 puertos en el target
    for x in range(1,80):
        t = threading.Thread(target=analyze_port, args=('192.168.30.157', x, sem))
        threads.append(t)
        t.start()
        sem.acquire()
    #Esperamos a que todos los hilos finalicen
    for x in threads:
        x.join()
    #Mostrando los resultados
    print "[]"
    for x in OPEN_PORTS:
        print "         - %s/TCP" % x

if __name__ == '__main__':
    main()
