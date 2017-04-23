#!/usr/bin/env/python2
#-*- coding: utf-8 -*-

import subprocess
import shlex

cmd_line = "ping -c www.google.com"
args = shlex.split(cmd_line)
try:
    subprocess.check_call(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print "[+] Google server is up"
except subprocess.CalledProcessError, e:
    print "[-] Failed: %s" % e