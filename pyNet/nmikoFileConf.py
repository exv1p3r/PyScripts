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

iosv_l2_s4 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.103',
	'username': 'gh0st',
	'password': 'p455w0rd',
}

iosv_l2_s5 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.104',
	'username': 'gh0st',
	'password': 'p455w0rd',
}

with open('ios_commands') as f:
	lines = f.read().splitlines()
print lines

all_dev = [iosv_l2_s1, iosv_l2_s2, iosv_l2_s3, iosv_l2_s4, iosv_l2_s5]

for devices in all_dev:
	net_connect = ConnectHandler(**devices)
	of = net_connect.send_config_set(lines)
	print of