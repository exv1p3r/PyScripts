#!/usr/bin/env python2
#-*-coding: utf-8-*-#
import smtplib #Importamos la librería
mail_server = 'mail.dextratech.com' #Declaramos el servidor de correo
mail_srv_port = 587 #Declaramos el puerto que va a usar el server de correo
from_addr = 'edson.cervantes@dextratech.com' #Declaramos la dirección de la cual queremos enviar el email
to_addr = 'rodolfo.pimentel@dextratech.com' #Hacia quien va dirigido el correo

from_header = 'From: %s\r\n' % from_addr 
to_header = 'To: %s\r\n' % to_addr
subject_header = 'Subject: VPN config' #Asunto del email
body = 'Estos son los datos para una configuracion correcta en el VPN' #Cuerpo/composicion del email

email_message = '%s\n%s\n%s\n\n%s' % (from_header, to_header, subject_header, body) 

s = smtplib.SMTP(mail_server, mail_srv_port) #Usamos la función SMTP para indicar el server y el puerto que queremos usar
s.sendmail(from_addr, to_addr, email_message) #Funcion sendmail, toma 3 params: quien lo manda, quien recibe y el email per se
s.quit()