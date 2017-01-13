#!/usr/bin/env python2
import subprocess
import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

def disk_report():
    p = subprocess.Popen("df -h", shell=True, 
                          stdout=subprocess.PIPE)
    return p.stdout.readlines()

def create_pdf(input, output="disk_report.pdf"):
    now = datetime.datetime.today()
    date = now.strftime("%h ")