#!/usr/bin/env python2
import smtplib
mail_srv = 'mail.dextratech.com'
mail_srv_port = 587

from_addr = 'foo@example.com'
to_addr = 'foo2@example.com'

from_header = 'From: %s\r\n' % from_addr
to_header = 'To: %s\r\n' % to_addr
subject_header = 'Subject: Test SMTP auth'
body = 'Email para calar la autenticacion SMTP'

email_msg = '%s\n%s\n%s\n\n%s' % (from_header, to_header, subject_header, body)

s = smtplib.SMTP(mail_srv, mail_srv_port)
s.set_debuglevel(1)
s.starttls()
s.login('fatalbert', 'mysecretpasswd')
s.sendmail(from_addr, to_addr, email_msg)
s.quit()