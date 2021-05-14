
from netmiko import ConnectHandler

username = "arista"
password = "arista"


dev = ["10.73.1.101", "10.73.1.102","10.73.1.105","10.73.1.10.6",  "10.73.1.107", "10.73.1.108"]

cfg_file = "config.txt"

for ip in dev: 
  switch = {'device_type': 'arista_eos', 'host': ip, 'username': username, 'password': password, 'port': '22', 'timeout': 180}
  connection = ConnectHandler(**switch)
  # connection.is_alive()
  connection.enable()
  connection.send_config_from_file(cfg_file)
  connection.disconnect()

