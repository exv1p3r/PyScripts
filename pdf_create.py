#!/usr/bin/env python2

from reportlab.pdfgen import canvas

def hello():
    c = canvas.Canvas("helloworld.pdf")
    c.drawString(100,100,"Hello World!")
    c.showPage()
    c.save()

hello()