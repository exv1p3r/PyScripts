#!/usr/bin/env python2
import paramiko
import os

host = ''
port = 2022
username = ''
password = ''
dir_path = '/home/root/logs'

def main():
    t = paramiko.Transport((host, port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    files = sftp.listdir(dir_path)
    for f in files:
        print '[*] Retrieving', f
        sftp.get(os.path.join(dir_path, f), f)
    t.close()

if __name__ == '__main__':
    main()