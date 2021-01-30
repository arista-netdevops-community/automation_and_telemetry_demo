from jsonrpclib import Server
from pprint import pprint as pp

username = "arista"
password = "arista"
ip = ["172.28.135.38", "172.28.135.39", "172.28.135.145", "172.28.134.246", "172.28.128.69", "172.28.134.80", "172.28.132.154"]
commands_list = ["sho syst environ tempera", "sh ver"]

for dev in ip:
    url = "http://" + username + ":" + password + "@" + dev + "/command-api"
    switch = Server(url)
    try:
        result=switch.runCmds(version=1,cmds=commands_list, format='json', autoComplete=True)
    except :
        print("cannot execute these commands using eapi on the device " + dev)
    else: 
        print ("device ip is {}, temperature status is {}, eos version is {}, model is {}".format(dev, result[0]['systemStatus'], result[1]['version'], result[1]['modelName']))

