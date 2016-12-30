#!/usr/bin/env python2
"""
Uso:

apache_log_parser_regex.py algun_archivo_log

Este scripts toma un argumento en la linea de comandos: el nombre de un
log a 'parsear'. Entonces lo 'parsea' y genera un reporte que asocia el
host remoto con el numero de bytes transferidos a el 
"""

import sys
import re
log_line_re = re.compile(r'''(?P<remote_host>\S+)
                            \s+ #whitespace
                            \S+ #remote logname
                            \s+ #whitespace
                            \S+ #remote user
                            \s+ #whitespace
                            \[[^\[\]]+\] #time
                            \s+ #whitespace
                            "[^"]+" #first line of request
                            \s+ #whitespace
                            (?P<status>\d+)
                            \s+ #whitespace
                            (?P<bytes_sent>-|\d+)
                            \s* #whitespace
                            ''', re.VERBOSE)
def dictify_logline(line):
    '''
    Regresa un diccionario de las piezas de un log de apache

    Actualmente los unicos campos en los que estamos interesados 
    son el host remoto y el numero de bytes enviados, pero estamos
    poniendo el 'status' solo por las buenas practicas.
    '''
    m = log_line_re.match(line)
    if m:
        groupdict = m.groupdict()
        if groupdict['bytes_sent'] == '-':
            groupdict['bytes_sent'] = '0'
        return groupdict
    else:
        return{'remote_host': None,
                'status': None,
                'bytes_sent': "0",
              }
def generate_log_report(logfile):
    '''
    Regresa un diccionario de formato: remote_host=>[list of bytes sent]

    Esta funcion toma un objeto archivo, concatena a traves de las lineas en el archivo,
    y genera un reporte de el numero de bytes tranferidos a cada host remoto por cada "hit"
    en el servidor web.
    '''
    report_dict = {}
    for line in logfile:
        line_dict = dictify_logline(line)
        print line_dict
        try:
            bytes_sent = int(line_dict['bytes_sent'])
        except ValueError:
            ##totalmente en desacuerdo con algo que no podemos entender
            continue
        report_dict.setdefault(line_dict['remote_host'], []).append(bytes_sent)
    return report_dict

if __name__ == '__main__':
    if not len(sys.argv) > 1:
        print __doc__
        sys.exit(1)
    infile_name = sys.argv[1]
    try:
        infile = open(infile_name, 'r')
    except IOError:
        print "Debes especificar un archivo valido"
        print __doc__
        sys.exit(1)
    log_report = generate_log_report(infile)
    infile.close()
    