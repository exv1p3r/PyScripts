#!/usr/bin/env python
#Python network programming cookbook - Chapter 1.11

import ntplib
from time import ctime

def print_time():
    ntp_client = ntplib.NTPClient()
    response = ntp_client.request('north-america.pool.ntp.org')
    print ctime(response.tx_time)

if __name__ == '__main__':
    print_time()
