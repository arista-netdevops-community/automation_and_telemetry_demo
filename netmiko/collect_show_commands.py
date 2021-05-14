from netmiko import ConnectHandler
import os

username = "ansible"
password = "ansible"
ip = "10.73.1.105"
commands = ["show version", "show ip interface brief"]

switch = {'device_type': 'arista_eos', 'host': ip, 'username': username, 'password': password, 'port': '22', 'timeout': 180}
connection = ConnectHandler(**switch)
connection.is_alive()
for command in commands:
    cmd_output = connection.send_command(command)
    f=open(command + ".txt", "w")
    f.write(cmd_output)
    f.close

connection.disconnect()

