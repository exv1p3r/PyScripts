#!/usr/bin/env python2
import getpass
import sys
import telnetlib

HOST = "192.168.122.10"
user = raw_input("Enter your telnet account: ")
password = getpass.getpass()

# Connection using the telnetlib
tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

# Cisco configuration
tn.write("enable\n")
tn.write("cisco\n")
tn.write("conf t\n")
tn.write("vlan 10\n")
tn.write("name Administracion\n")
tn.write("vlan 20\n")
tn.write("name Ingenieria\n")
tn.write("vlan 30\n")
tn.write("name Marketing\n")
tn.write("vlan 40\n")
tn.write("name Recursos_Humanos\n")
tn.write("int loopback 0\n")
tn.write("ip addr 1.1.1.1 255.255.255.0\n")
tn.write("end\n")
tn.write("exit\n")

print tn.read_all()
