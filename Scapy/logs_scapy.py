#!/usr/bin/env python2
import logging
import logging.handlers

from scapy.all import IP, TCP, sr1

#Inicializacion del log
logger = logging.getLogger(__name__)

#Nivel del log
logger.setLevel(logging.DEBUG)
#formatter = logging.Formatter('[%(levelname)s] % (message)s')
formatter = logging.Formatter('(%(asctime)s) % (message)s')

#Manejador: Salida por fichero de texto
log_file = 
logging.FileHandler(filename="Scapy_log_1.2.3.7.2_2.txt")
log_file.setFormatter(formatter)

#Manejador: Salida por consola
log_console = logging.StreamHandler()
log_console.setFormatter(formatter)

#Configuracion del log remoto
log_syslog = logging.handlers.SysLogHandler(address=('mail.dextratech.com', 25))
log_syslog.setFormatter(formatter)

#Agregaremos todos los manejadores a la configuracion del log
logger.addHandler(log_syslog)
logger.addHandler(log_console)
logger.addHandler(log_file)

OPEN_PORTS = []

def analyze_port(tgt, port):
    logger.info("   - Analizando puerto %s" % port)
    res = sr1(IP(dst=tgt)/TCP(dport=port,, flags='S'), verbose=False, timeout=0.2)

    if res:
        if res[TCP.flags == 18]:
            logger.info("   |_ Puerto %s abierto" % port)
            OPEN_PORTS.append(port)
        else:
            logger.debug("  |_ Puerto %s cerrado" % port)

def main():
    logger.info("[*] Iniciando escaneo")
    #Analizando los primeros 80 puertos
    for x in range(20, 80):
        analyze_port("192.168.30."+x)
    logger.info("[*] Escaneo finalizado")

    #Mostramos los resultados
    logger.info("[*] Lista de puertos abiertos")
    for x in OPEN_PORTS:
        logger.critical("   -%s/TCP" % x)
    else:
        logger.critical("[!] No se han encontrado puertos abiertos")

def xmain():
    #Level: info
    logger.info("This is a message")

    #Level: debug
    logger.debug("This is a message")

    #Level: Error
    logger.error("This is a message")

if __name__ == '__main__':
    main()