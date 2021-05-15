from jsonrpclib import Server
username = "arista"
password = "arista"
ip = "10.73.1.101"
url = "http://" + username + ":" + password + "@" + ip + "/command-api"
switch = Server(url)
commands_list = ["show ip route summary"]
result=switch.runCmds(version=1,cmds=commands_list, format='json', autoComplete=True)
result[0]["totalRoutes"]
