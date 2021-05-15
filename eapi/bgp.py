from jsonrpclib import Server
username = "ansible"
password = "ansible"
ip="10.73.1.101"
url = "http://" + username + ":" + password + "@" + ip + "/command-api"
print(url)
switch = Server(url)
result=switch.runCmds(version=1,cmds=["show ip bgp neighbors"])
for item in result[0]['vrfs']['default']['peerList']:  
   print ("the BGP session with " + item['peerAddress'] + " is " + item['state'])
