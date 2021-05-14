from jsonrpclib import Server
from pprint import pprint as pp

username = "arista"
password = "arista"
ip = ["10.73.1.101","10.73.1.102", "10.73.1.105", "10.73.1.106", "10.73.1.107", "10.73.1.108"]

for dev in ip: 
    url = "http://" + username + ":" + password + "@" + dev + "/command-api"
    switch = Server(url)
    try:
        result=switch.runCmds(version=1,cmds=["show version"])
    except :
        print("cannot execute this command using eapi on the device " + dev)
    else: 
        pp(result[0])

