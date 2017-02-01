#!/usr/bin/env python2
#-*- coding: utf-8 -*-#

host = ''
port = 2022
user = ''
passwd = ''
pkey_file = ''
def main():
    key = paramiko.RSAKey.from_private_key_file(pkey_file)
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.connect(host, port, pkey=key)
    stdin, stdout, stderr = s.exec_command('ifconfig')
    print stdout.read()
    s.close()

if __name__ == '__main__':
    main()