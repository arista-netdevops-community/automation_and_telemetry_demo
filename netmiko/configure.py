
from netmiko import ConnectHandler

username = "arista"
password = "arista"
ip = "172.28.131.231"

cfg_file = "config.txt"

switch = {'device_type': 'arista_eos', 'host': ip, 'username': username, 'password': password, 'port': '22', 'timeout': 180}
connection = ConnectHandler(**switch)
# connection.is_alive()
connection.enable()
connection.send_config_from_file(cfg_file)
connection.disconnect()

