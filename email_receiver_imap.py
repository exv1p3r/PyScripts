#!/usr/bin/pytho2
import imaplib

username = 'someuser'
passwd = '7ops3cr3t'

mail_server = 'mail.dextratech.com'

i = imaplib.IMAP4_SSL(mail_server)
print i.login(username, passwd)
print i.select('INBOX')
for msg_id in i.search(None, 'ALL')[1][0].split():
    print msg_id
    outf = open('%s.eml' % msg_id, 'w')
    outf.write(i.fetch(msg_id, '(RFC822)')[1][0][1])
    outf.close()
i.logout()