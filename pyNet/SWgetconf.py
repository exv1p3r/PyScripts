#!/usr/bin/env python2
import getpass
import telnetlib

# Credentials needed to the telnet connection
user = raw_input("Enter your telnet account: ")
password = getpass.getpass()

#Open the file which has the IP address of the devices
f = open('switches.txt')

# Put the IP addrs to loop the conn
for line in f:
    print "[+] Getting config from switch: " + line 
    HOST = line.strip()
    # Connection using the telnetlib
    tn = telnetlib.Telnet(HOST)
    tn.read_until("Username: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")

    # Cisco configuration
    # "terminal length 0" command show us the whole config in a device
    tn.write("terminal length 0\n")
    tn.write("sh run\n")
    tn.write("exit\n")

    readoutput = tn.read_all()
    saveoutput = open("switchConf_" + HOST, "w")
    saveoutput.write(readoutput)
    saveoutput.close()
