#!/usr/bin/env python2
#-*- coding: utf-8 -*-#
################################################
# Script para verificar la existencia de algun #
# recurso en un servidor web                   #
# Created by: exv1p3r                          #
################################################
import httplib
import sys

def check_webserver(addr, port, resource):
    #Crear la conexion
    if not resource.startswith('/'):
        resource = '/' + resource
    try:
        conn = httplib.HTTPConnection(addr, port)
        print 'HTTP connection created succesfully'
        #Hacer la peticion
        req = conn.request('GET', resource)
        print 'Request for %s was succesfull' % resource
        #Respuesta GET 
        resp = conn.getresponse()
        print 'Response status: %s' % resp.status
    except sock.error, e:
        print 'HTTP connection failed: %s' % e
        return False
    finally:
        conn.close()
        print "HTTP connection closed succesfully"
    if resp.status in [200, 301]:
        return True
    else:
        return False

if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option('-a', '--address', dest='addr', default='localhost', help='Address for webserver')
    parser.add_option('-p', '--port', dest='port', type='int', default=80, help='Port for webserver')
    parser.add_option('-r', '--resource', dest='resource', default='index.html', help='Resource to check')
    (options, args) = parser.parse_args()
    print 'Options: %s, args: %s' % (options, args)
    check = check_webserver(options.addr, options.port, options.resource)
    print 'check_webserver returned: %s' % check
    sys.exit(not check)