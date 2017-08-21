#!/usr/bin/env python2
from scapy.all import *
import os
import sys
import threading
import signal

iface = "en1"
tgt_ip = "" 