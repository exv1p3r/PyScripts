#!/usr/bin/env python2
import getpass
import sys
import telnetlib

HOST = "192.168.122.6"
user = raw_input("Enter your telnet account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("enable\n")
tn.write("qazwsx123\n")
tn.write("conf t\n")
tn.write("int loopback 0\n")
tn.write("ip addr 1.1.1.1 255.255.255.0\n")
tn.write("enable\n")
tn.write("exit\n")

print tn.read_all()
