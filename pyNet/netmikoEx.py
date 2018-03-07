#!/usr/bin/env python2
from netmiko import ConnectHandler

iosv_l2 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.122.100',
	'username': 'gh0st',
	'password': 'cisco',
}

net_connect = ConnectHandler(**iosv_l2)

output = net_connect.send_command('sh ip int br')
print output

config_cmds = ['int loop 0', 'ip addr 1.1.1.1 255.255.255.0']
output = net_connect.send_config_set(config_cmds)
print output

for n in range(2,16):
	print "[*] Creating VLAN: " + str(n)
	config_cmds = ['vlan '+ str(n), 'name pyVlan_' + str(n)]
	output = net_connect.send_config_set(config_cmds)
	print output
