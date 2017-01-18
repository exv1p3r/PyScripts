#!/usr/bin/env python2
#-*- coding utf-8 -*-#
#Importamos las dos librerias necesarias
import gdchart
import shelve

#Abrimos el archivo que creamos anteriormente
shelve_file = shelve.access('access.s')
#El objeto shelve es un diccionario, vamos a llamar el método Items() 
items_list = [(i[1], i[0]) for i in shelve_file.items()]
#Regresa una lista de tuplas en las cuales el primer elemento de ella es
# la llave del diccionario y el segundo elemento es el valor 
items_list.sort()
#Podemos usar el método items() para acomodar los datos de forma que tengan
#mayor sentido cuando son impresos
bytes_sent = [i[0] for i in items_list]
#ip_addresses = [i[1] for i in items_list]
ip_addresses = ['XXX.XXX.XXX.XXX' for i in items_list]

chart = gdchart.Bar()
chart.width = 400
chart.height = 400
chart.bg_color = 'white'
chart.plot_color = 'black'
chart.xtitle = 'IP Address'
chart.ytitle = 'Bytes sent'
chart.title = 'Usage by IP Address'
chart.setData(bytes_sent)
chart.setLabels(ip_addresses)
chart.draw('bytes_ip_bar.png')

shelve.close()