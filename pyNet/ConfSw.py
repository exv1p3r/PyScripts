#!/usr/bin/env python2
import telnetlib
import getpass
import sys

user = raw_input("Enter your telnet account: ")
passwd = getpass.getpass()

f = open("switches.txt")

for device in f:
	print "[*] Telnet to host: " + str(device)
	HOST = device

	# Telnet connect
	tn = telnetlib.Telnet(HOST)
	tn.read_until("Username: ")
	tn.write(user + '\n')
	if password:
		tn.read_until()
		tn.write(passwd)

	