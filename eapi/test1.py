from jsonrpclib import Server
from pprint import pprint as pp

username = "arista"
password = "arista"
ip = ["172.28.135.38", "172.28.135.39", "172.28.135.145", "172.28.134.246", "172.28.128.69", "172.28.134.80", "172.28.132.154"]

for dev in ip: 
    url = "http://" + username + ":" + password + "@" + dev + "/command-api"
    switch = Server(url)
    try:
        result=switch.runCmds(version=1,cmds=["show version"])
    except :
        print("cannot execute this command using eapi on the device " + dev)
    else: 
        pp(result[0])

