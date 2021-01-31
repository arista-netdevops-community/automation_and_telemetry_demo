from netmiko import ConnectHandler
import os 

username = "arista"
password = "arista"
ip = "172.28.131.231"
command = "show version"

switch = {'device_type': 'arista_eos', 'host': ip, 'username': username, 'password': password, 'port': '22', 'timeout': 180}
connection = ConnectHandler(**switch)
connection.is_alive()
cmd_output = connection.send_command(command)
f=open(command + ".txt", "w")
f.write(cmd_output)
f.close
connection.disconnect()

