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
tn.write("conf t\n")
for n in range(2, 10):
    tn.write("vlan " + str(n) + "\n")
    tn.write("name vlan_" + str(n) + "\n")
tn.write("end\n")
tn.write("exit\n")

print tn.read_all()
