#!/usr/bin/env python2
import nmap
import optparse
def nmapScan(tgtHost, tgtPort):
    nmScan = nmap.PortScanner()
    nmScan.scan(tgtHost, tgtPort)
    for port in tgtPort:
        state = nmScan['scan'][tgtHost]['tcp'][port]
        print "[*] " + tgtHost + "tcp/" + tgtPort + " " + state
def main():
    parser = optparse.OptionParser('Usage: %prog '+\
    '-H <target host> -p <target port>')
    parser.add_option('-H', dest=tgtHost, type='string', help='Specify tgt host')
    parser.add_option('-p', dest=tgtPort, type='string', help='specify tgt port[s] separated by a comma')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPort = str(options.tgtPort).split(', ')
    if (tgtHost == None) | (tgtPort[0] == None):
        print parser.usage
        exit(0)
    for tgtPorts in tgtPort:
        nmapScan(tgtHost, tgtPorts)
if __name__ == 'main':
    main()
    