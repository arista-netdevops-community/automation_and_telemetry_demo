from jsonrpclib import Server
from pprint import pprint as pp

username = "arista"
password = "arista"
ip = ["10.73.1.101","10.73.1.102", "10.73.1.105", "10.73.1.106", "10.73.1.107", "10.73.1.108"]


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

