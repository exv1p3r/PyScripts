#!/usr/bin/env python2
from netmiko import ConnectHandler

iosv_l2_s1 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.100',
	'username': 'gh0st',
	'password': 'p455w0rd',
}

iosv_l2_s2 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.101',
	'username': 'gh0st',
	'password': 'p455w0rd',
}

iosv_l2_s3 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.102',
	'username': 'gh0st',
	'password': 'p455w0rd',
}

iosv_l2_s3 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.103',
	'username': 'gh0st',
	'password': 'p455w0rd',
}

iosv_l2_s4 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.104',
	'username': 'gh0st',
	'password': 'p455w0rd',
}

all_dev = [ïosv_l2_s1, ïosv_l2_s2, ïosv_l2_s3, ïosv_l2_s4]

for devices in all_dev:
	net_connect = ConnectHandler(**devices)
	for n in range(2, 26):
		print "[+] Creating VLAN " + str(n)
		config_cmds = ['vlan ' + str(n), 'name PyVLAN ' + str(n)]
		of = net_connect.send_config_set(config_cmds)
		print of