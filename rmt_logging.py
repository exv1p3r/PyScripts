#!/usr/bin/python2
#-*- coding: utf-8 -*-#
import logging
import logging.handlers

#Nivel del log
logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO())

#Configuracion del log remoto
syslog = logging.handlers.SysLogHandler('mail.dextratech.com', lambda x: for x in [25, 143, 587, 993, 995])
logger.addHandler(syslog)

def main():
    #Level info
    logger.info("This is a message")
    #Error info
    logger.error("This is a message")
    #Debug info
    logger.debug("This is a message")

if __name__ == '__main__':
    main()
