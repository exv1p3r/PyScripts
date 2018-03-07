#!/usr/bin/env python2
import getpass
import sys
import telnetlib

HOST = "192.168.122.80"
user = raw_input("Username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("enable\n")
tn.write("p455w0rd\n")
tn.write("conf t\n")
tn.write("vlan 2\n")
tn.write("name pyVLAN_2\n")
tn.write("exit\n")
tn.write("vlan 3\n")
tn.write("name pyVLAN_3\n")
tn.write("exit\n")
tn.write("vlan 4\n")
tn.write("name pyVLAN_4\n")
tn.write("exit\n")
tn.write("vlan 5\n")
tn.write("name pyVLAN_5\n")
tn.write("end\n")
tn.write("wr\n")
tn.write("exit\n")

print tn.read_all()