#!/usr/bin/env python2
import requests
import urllib
import urllib2

ID_USERNAME = 'signup-username'
ID_EMAIL = 'signup-email'
ID_PASSWORD = 'signup-user-password'
USERNAME = 'username'
EMAIL = 'correo@servidorcorreo.com'
PASSWORD = 'nuestro passwd'
SIGNUP_URL = 'https://twitter.com/account/create'

def submit_form():
    