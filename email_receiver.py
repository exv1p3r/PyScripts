#!/usr/bin/python2
import poplib

username = 'someuser@dextratech.com'
passwd = 's3cr3t'

mail_srv = 'mail.dextratech.com'

#Primero definimos el tipo de servidor (POP3), usuario y passwd
p = poplib.POP3(mail_srv)
p.user(username)
p.pass_(passwd)
for msg in p.list()[1]:
    print msg
    outf = open('%s.eml' % msg, 'w')
    outf.write('\n'.join(p.retr(msg)[1]))
    outf.close()
p.quit()