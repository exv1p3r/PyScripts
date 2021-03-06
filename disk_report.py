#!/usr/bin/python2
#-*- coding: utf-8 -*-#

import subprocess
import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

def disk_report():
    p = subprocess.Popen("df -h", shell=True, stdout=subprocess.PIPE)
    return p.stdout.readlines()

def create_pdf(input, output="disk_report.pdf"):
    now = datetime.datetime.today()
    date = now.strftime("%h &d %y %H:%D:%S")
    c = canvas.Canvas(output)
    textobject = c.beginText()
    textobject.setTextOrigin(inch, 11*inch)
    textobject.textLines('''
    Disk capacity report: %s
    ''' %date)
    for line in input:
        textobject.textLine(line.strip())
    c.drawText(textobject)
    c.showPage()
    c.save()
report = disk_report()
create_pdf(report)

