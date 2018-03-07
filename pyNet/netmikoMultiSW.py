#!/usr/bin/env python2
from netmiko import ConnectHandler

iosv_L2_1 = {
	"device_type": "cisco_ios",
	"ip": "192.168.122.80",
	"username": "gh0st",
	"password": "p455w0rd",
}

iosv_L2_2 = {
	"device_type": "cisco_ios",
	"ip": "192.168.122.90",
	"username": "gh0st",
	"password": "p455w0rd",
}

iosv_L2_3 = {
	"device_type": "cisco_ios",
	"ip": "192.168.122.100",
	"username": "gh0st",
	"password": "p455w0rd",
}

all_devices = [iosv_L2_1, iosv_L2_2, iosv_L2_3]

for device in all_devices:
	net_connect = ConnectHandler(**device)
	for n in range(2,30):
		print "[*] Creating VLAN " + str(n)
		config_cmds = ['vlan ' + str(n), 'name pyVLAN_' + str(n)]
		output = net_connect.send_config_set(config_cmds)
		print output