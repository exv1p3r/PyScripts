#!/usr/bin/env python2
import paramiko
import time

ip_addr = '192.168.122.100'
user = 'gh0st'
passwd = 'cisco'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key(paramiko.AutoAddPolicy())
ssh.connect(hostname=ip_addr, username=user, password=passwd)

print "[*] Connection stablished: ", ip_addr

conn = ssh.invoke_shell()

conn.send("conf t\n")
conn.send("int loop 0\n")
conn.send("ip addr 1.1.1.1 255.255.255.0\n")
conn.send("int loop 1\n")
conn.send("ip addr 2.2.2.2 255.255.255.0\n")
# conn.send("router ospf 1\n")
# conn.send("network 0.0.0.0 255.255.255.255 area 0\n")

for n in range(2, 21):
	print "[*] Creating VLAN " + str(n)
	conn.send('vlan ' + str(n) + '\n')
	conn.send('name pyVlan + ' + str(n) + "\n")
	time.sleep(0.5)


conn.send('end\n')

time.sleep(1)
output = conn.recv(65535)
print output

ssh.close