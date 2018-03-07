#!/usr/bin/env python2
import json
from napalm import get_network_driver

driver = get_network_driver('ios')
iosvl2 = driver('192.168.122.100', 'gh0st', 'cisco')
iosvl2.open()

output = iosvl2.get_facts()
print (json.dumps(output, sort_keys=True, indent=4))


output1 = iosvl2.get_interfaces()
print (json.dumps(output1, sort_keys=True, indent=4))


output2 = iosvl2.get_interfaces_counters()
print (json.dumps(output2, sort_keys=True, indent=4))