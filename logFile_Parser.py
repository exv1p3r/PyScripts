#!/usr/bin/env python2
import sys
def dictify_logline(line):
    split_line = line.split()
    return
    {
    '''
    Refresa yb diccionario de las pieces pertinentes de un log de apache.

    Actualmente, los unicos camps en los que estamos realmente interesados son
    en el host remoto y en los bytes enviados, pero tambien estamos poniendo
    estaods ahi solo por las buenas practicas
    '''
        'remote_host' : split_line[0],
        'status'      : split_line[8],
        'bytes_sent'  : split_line[9],
    }
def generate_log_report(logfile):
    '''
    Regresa un diccionaro de formato remote_host=>[list of bytes sent]

    Esta funcion toma como argumento un archivo, conjunta a traves de las lineas del
    archivo y genera un reporte de el numero de bytes transmitidos a cada host
    remoto para cada "hit" en el web server
    '''
    report_dict = {}
    for line in logfile:
        line_dict = dictify_logline(line)
        print line_dict
        try:
            bytes_sent = int(line_dict['bytes_sent'])
        except ValueError:
            continue
        report_dict.setdefault(line_dict['remote_host'], []).append(bytes_sent)
    return report_dict

if __name__ == '__main__':
    if not len(sys.argv) > 1: #Verificamos que el usuario haya puesto un argumento
        print __doc__         #Si no, imprimimos la ayuda
        sys.exit(1)
    infile_name = sys.argv[1] #Se toma el argumento, el cual es un archivo
    try:
        infile = open(infile_name, 'r') #Intentamos abrir el objeto para poder escribir en el
    except IOError:
        print "You must specify a valid file to parse."
        print __doc__
        sys.exit(1)
    log_report = generate_log_report(infile)
    print log_report
    infile.close()
