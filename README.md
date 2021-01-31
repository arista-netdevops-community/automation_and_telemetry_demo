## automation server

```
$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 18.04.1 LTS
Release:        18.04
Codename:       bionic
```
```
$ python3 -V
Python 3.6.9
```
change dns to 8.8.8.8
```
sudo vi /etc/netplan/50-cloud-init.yaml
sudo netplan apply
```
Run these commands
```
sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get install tree snmp python3-pip build-essential libssl-dev libffi-dev python3-dev -y
pip3 install napalm netmiko jsonrpclib-pelix pyang pyangbind ansible==2.9.15 influxdb
```
Then:
- install docker (https://docs.docker.com/engine/install/ubuntu/)
- install docker-compose (https://docs.docker.com/compose/install/)
- install gnmic (https://gnmic.kmrd.dev./#installation)

## EOS devices

Then configure all eos devices for gnmi and snmp and eapi:
```
snmp-server community public ro
username arista secret 0 arista
ip access-list GNMI
   10 permit tcp any any eq gnmi
management api gnmi
   transport grpc def
      ip access-group GNMI
   provider eos-native
management api http-commands
   protocol http
   no shutdown
```
Then configure one single eos device for isis lsdb streaming:
```
management api models
   provider smash
      path routing/isis/lsdb
```
```
dev(config-router-isis)#sho active  | grep pub
   database publish
```
Then restart octa on that swicth
```
bash sudo killall Octa
```

## snmp
```
snmpwalk -v 2c -c public 172.28.135.38 .1.3.6.1.2.1.1.3.0
```

## netmiko
```
cd netmiko
python3 test.py
more "show version.txt"
cd ..
```

## eapi
```
cd eapi
python3 test1.py
python3 test2.py
cd ..
```

## ansible
```
cd ansible
```
```
ansible-playbook playbooks/print_version_and_models.yml
```
```
ansible-playbook playbooks/snapshots.yml
tree snapshots
```
```
ansible-playbook playbooks/tests.yml
ls reports
more reports/POC-state.md 
```
```
cd ..
```
## pyang
```
git clone https://github.com/openconfig/public.git
mkdir yang_modules
cp public/release/models/*.yang yang_modules/.
cp -R public/release/models/*/*.yang yang_modules/.
cp public/third_party/ietf/*.yang yang_modules/.
```
```
cd yang_modules/
```
validate yang modules
```
pyang openconfig-bgp.yang
```
convert yang to yin
```
pyang openconfig-bgp.yang -f yin -o openconfig-bgp.yin
ls *.yin
```
get a tree
```
pyang -f tree openconfig-interfaces.yang
pyang openconfig-interfaces.yang -f tree --tree-path=/interfaces/interface/state
pyang openconfig-interfaces.yang -f tree  --tree-depth=4
```
```
cd ..
```
## pyangbind
```
cd yang_modules/
```
```
pyang --plugindir $HOME/.local/lib/python3.6/site-packages/pyangbind/plugin/ -f pybind -o oc_bgp.py openconfig-bgp.yang
ls oc_bgp.py
```
```
more pyangbind_demo.py
python3 pyangbind_demo.py
more ../test.json
```
```
cd ..
```

## gNMI

gnmi capabilities
```
gnmic -a 172.28.135.38:6030 -u arista -p arista --insecure capabilities
```

gnmi set
```
gnmic -a 172.28.131.231:6030 --insecure -u arista -p arista get --path "/interfaces/interface[name=Ethernet1]/config/description"
gnmic -a 172.28.131.231:6030 --insecure -u arista -p arista set --update-path "/interfaces/interface[name=Ethernet1]/config/description" --update-value "gnmi-example"
gnmic -a 172.28.131.231:6030 --insecure -u arista -p arista get --path "/interfaces/interface[name=Ethernet1]/config/description"
sh run int et1
```
```
gnmic -a 172.28.131.231:6030 --insecure -u arista -p arista set --update  "/interfaces/interface[name=Ethernet3]/config/enabled:::bool:::false"
gnmic -a 172.28.131.231:6030 --insecure -u arista -p arista get --path  "/interfaces/interface[name=Ethernet3]/config/enabled"
sh run int et3
```
pyangbind + gnmi
```
gnmic -a 172.28.131.231:6030 --insecure -u arista -p arista get --path '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP]/bgp'
```
```
sh run sec bgp
```
```
more test.json
```
```
gnmic -a 172.28.131.231:6030 --insecure -u arista -p arista set --replace-path '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP]/bgp' --replace-file test.json
gnmic -a 172.28.131.231:6030 --insecure -u arista -p arista get --path '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP]/bgp'
```
```
sh run sec bgp
```

gnmi sub
```
gnmic -a 172.28.135.38:6030 -u arista -p arista --insecure sub --path '/network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor[neighbor-address=::133:0:0:2]/state'
gnmic -a 172.28.135.38:6030 -u arista -p arista --insecure sub --path '/interfaces/interface[name=Ethernet1]/state/counters'
```
gnmi get
```
gnmic -a 172.28.135.38:6030 -u arista -p arista --insecure get --path  '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP]/bgp/neighbors'
gnmic -a 172.28.131.231:6030 -u arista -p arista --insecure get --path "/interfaces/interface[name=Ethernet3]/config/description"
```
sub to eos native
```
gnmic -a 172.28.135.38:6030 -u arista -p arista --insecure sub --path "eos_native:/Sysdb/routing/bgp/export/"
```

sub to isis lsdb
```
cd gnmi/ 
more gnmic_conf.yml
```
```
gnmic --config gnmic_conf.yml sub --path "eos_native:/Smash/routing/isis/lsdb/"
```
```
more gnmi_output.txt
```
OR
```
gnmic -a 172.28.135.38:6030 -u arista -p arista --insecure sub --path "eos_native:/Smash/routing/isis/lsdb/2/default/lsp" > redirect_output.txt
```
```
more redirect_output.txt
```
```
cd ..
```
## telegraf

use this telegraf fork in order to have Telegraf to overwrite the gnmi timestamp by its local time
more details https://gist.github.com/ksator/e36a1be086da6c2239c2c2c0eb9fe300
```
git clone https://github.com/rski/telegraf
cd telegraf
make docker-image
docker images
cd ..
```

## TIG

start TIG
```
cd TIG
more docker-compose.yml
ls dashboards
ls telegraf.d/
docker-compose up -d
docker-compose ps
docker ps
```
check telegraf logs
```
docker logs telegraf
```
query influxdb from cli
```
docker exec -it influxdb bash
influx
show database
use arista
SHOW MEASUREMENTS
```
```
SHOW TAG KEYS FROM "ifcounters"
SHOW TAG VALUES FROM "ifcounters" with KEY = "device"
SHOW TAG VALUES FROM "ifcounters" with KEY = "name" WHERE ("device" = 'ta373')
SELECT * FROM "ifcounters" WHERE "device" = 'ta373'  ORDER BY DESC LIMIT 3
SELECT "in_octets","out_octets", "name" FROM "ifcounters" WHERE "device" = 'ta373' ORDER BY DESC LIMIT 3
SELECT "in_octets","out_octets", "name" FROM "ifcounters" WHERE ("device" = 'ta373' AND "name"='Ethernet16' AND time >= now() - 120s)
SELECT "in_octets","out_octets", "name" FROM "ifcounters" WHERE ("device" = 'ta373' AND "name"=~/Ethernet.*/ AND time >= now() - 120s) GROUP BY "name"
SELECT mean("in_octets")*8 FROM "ifcounters" WHERE ("device" = 'ta373' AND "name" = 'Ethernet24' AND time >= now() - 10m)
SELECT mean("in_octets")*8 FROM "ifcounters" WHERE ("device" = 'ta373' AND "name" = 'Ethernet24' AND time >= now() - 10m) GROUP BY time(1m)
SELECT derivative(mean("in_octets"), 1s) *8 FROM "ifcounters" WHERE ("device" = 'ta373' AND "name" = 'Ethernet24' AND time >= now() - 10m) GROUP BY time(1m)
SELECT derivative(mean("in_unicast_pkts"), 1s) FROM "ifcounters" WHERE ("device" = 'ta373' AND "name" = 'Ethernet4') AND (time >= now() - 10m)  GROUP BY time(1m)
SELECT stddev("in_octets") FROM "ifcounters" WHERE ("device" = 'ta373' AND ("name" = 'Ethernet1' OR "name" = 'Ethernet2') AND (time >= now() - 10m)) GROUP BY time(1m)
SELECT derivative(stddev("out_octets"), 1s)  / 8 FROM "ifcounters" WHERE ("device" =~ /ta.*/ AND "name" =~ /Ethernet[1|2]/ AND (time >= now() - 10m)) GROUP BY time(1m), "device"
```
```
SHOW TAG KEYS FROM "openconfig_bgp"
SHOW TAG VALUES FROM "openconfig_bgp" WITH KEY = "device"
SHOW TAG VALUES FROM "openconfig_bgp" WITH KEY = "neighbor_address" WHERE "device"='ta366'
SELECT LAST("neighbors/neighbor/state/session_state") FROM "openconfig_bgp" WHERE ("device"='ta366' AND "neighbor_address" = '132.0.0.2')
SELECT "device", "neighbor_address", LAST("neighbors/neighbor/state/session_state") AS session_state FROM "openconfig_bgp" WHERE ("device"='ta366' AND "neighbor_address" = '132.0.0.2')
SELECT LAST("neighbors/neighbor/state/session_state") FROM "openconfig_bgp" WHERE ("device"='ta366') GROUP BY neighbor_address
SELECT LAST("neighbors/neighbor/state/session_state") AS session_state FROM "openconfig_bgp" GROUP BY "device", "neighbor_address"
```
```
exit
exit
```

query influxdb from python
```
from influxdb import InfluxDBClient
influx_client = InfluxDBClient('localhost',8086)
influx_client.query('show databases')
influx_client.query('show measurements', database='arista')
points = influx_client.query("""SELECT "in_octets" FROM "ifcounters" WHERE ("device"='ta366' AND "name"='Ethernet24') ORDER BY DESC LIMIT 3""", database='arista').get_points()
points = influx_client.query("""SELECT "in_octets" FROM "ifcounters" WHERE ("device"='ta366' AND "name"='Ethernet24') ORDER BY DESC LIMIT 3""", database='arista').get_points()
for point in points:
     print(point['in_octets'])

exit()
```

grafana dashboards (arista/arista)
http://172.28.135.156:3000/login

stop TIG
```
docker-compose down
```


