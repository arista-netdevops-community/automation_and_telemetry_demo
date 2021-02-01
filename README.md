## Agenda

- Ansible demo  
- AVD end to end demo using eAPI (this demo is not covered in this repo) 
- YANG/gNMI presentation
- Pyang/Pyangbind/gnmic/TIG stack demo 

## Ubuntu VM from POC lab 

```
$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 18.04.1 LTS
Release:        18.04
Codename:       bionic
```
Change DNS to 8.8.8.8 so you can resolve domain names  
```
sudo vi /etc/netplan/50-cloud-init.yaml
sudo netplan apply
ping www.google.com
```
Now you can run these commands to update the VM and install tools
```
sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get install tree snmp python3-pip build-essential libssl-dev libffi-dev python3-dev -y
pip3 install napalm netmiko jsonrpclib-pelix pyang pyangbind ansible==2.9.15 influxdb
```
Check 
```
pip3 list
```
```
$ python3 -V
Python 3.6.9
```

If `ansible --version` or ` pyang --version` doesnt work, check the PATH env var: 
```
echo $PATH
```
try
```
/home/arista/.local/bin/ansible --version
```
then update accordingly the PATH env var: 
```
export PATH="$PATH:/home/arista/.local/bin"
echo $PATH
```
```
ansible --version
```

Then install also:
- docker (https://docs.docker.com/engine/install/ubuntu/)
- docker-compose (https://docs.docker.com/compose/install/)
- gnmic (https://gnmic.kmrd.dev./#installation) 
   - if gnmic installation fails: 
   ```
   wget https://github.com/karimra/gnmic/raw/master/install.sh
   sudo bash install.sh 
   ```

## Clone this repository 

```
git clone https://github.com/ksator/automation_and_telemetry_workshop.git
```
```
cd automation_and_telemetry_workshop
```

## Configure EOS devices

### Configure all EOS devices for gNMI and SNMP and eAPI
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
### Configure one single EOS device for ISIS LSDB streaming
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

## SNMP
```
snmpwalk -v 2c -c public 172.28.135.38 .1.3.6.1.2.1.1.3.0
```

## [Netmiko](netmiko)

Netmiko is a python library to simplify SSH connections to network devices

From the root of this repository: 
```
cd netmiko
```
```
python3 test.py
more "show version.txt"
```

## [eAPI](eapi)

From the root of this repository: 
```
cd eapi
```
```
python3 test1.py
python3 test2.py
```

## [Ansible](ansible)

From the root of the repository: 
```
cd ansible
ls
```

### Basic demo 
```
ansible-playbook playbooks/print_version_and_models.yml
```

### Test the devices (ntp, lldp, temperature, ...) and generate a report

To run all the tests: 
```
ansible-playbook playbooks/tests.yml
```
```
ls reports
more reports/POC-state.md 
more reports/POC-state.csv
```

To run all only some tests, use ansible tags. Example:  
```
ansible-playbook playbooks/tests.yml --tags lldp
```

### Collect show commands from the devices

Update the list of show commands you want to collect (ansible variable) and execute this playbook: 
```
ansible-playbook playbooks/snapshots.yml
tree snapshots
```

## pyang 

pyang is a python program.
We can use it to:
- Validate YANG modules against YANG RFCs
- Convert YANG modules into equivalent YIN module (XML)
- Generate a tree representation of YANG models for quick visualization

```
pip3 freeze | grep pyang
```

### Clone the openconfig repository

From the root of this repository: 
```
git clone https://github.com/openconfig/public.git
```
```
ls public
```

### Move all the YANG files from OpenConfig to the same directory

```
cp public/release/models/*.yang yang_modules/.
cp -R public/release/models/*/*.yang yang_modules/.
cp public/third_party/ietf/*.yang yang_modules/.
```
```
cd yang_modules/
ls
```

### Validate yang modules

```
pyang openconfig-bgp.yang
pyang openconfig-interfaces.yang
```

### Convert a YANG module into an equivalent YIN module

A YANG module can be translated into an XML syntax called YIN. The translated module is called a YIN module. The YANG and YIN formats contain equivalent information using different notations: YIN is YANG in XML. A YANG module can be translated into YIN syntax without losing any information.

Example (openconfig-bgp.yin is the YIN equivalent of openconfig-bgp.yang)

```
pyang openconfig-bgp.yang -f yin -o openconfig-bgp.yin
ls *.yin
```
### Generate a tree representation of YANG modules for quick visualization

```
pyang -f tree openconfig-interfaces.yang
pyang openconfig-interfaces.yang -f tree --tree-path=/interfaces/interface/state
pyang openconfig-interfaces.yang -f tree  --tree-depth=4
```

## PyangBind

PyangBind is a pyang plugin.  
It generates Python classes from a YANG module: It converts YANG module into a Python module, such that Python can be used to generate data which conforms with the data model defined in YANG.  

```
pip3 freeze | grep pyang
```

From the root of this repository: 
```
cd yang_modules/
```

### Converts a YANG module into a Python module

```
pyang --plugindir $HOME/.local/lib/python3.6/site-packages/pyangbind/plugin/ -f pybind -o oc_bgp.py openconfig-bgp.yang
```
```
ls oc_bgp.py
```

### Use the new python module to generate OpenConfig configuration 

```
more pyangbind_demo.py
python3 pyangbind_demo.py
```
It generated this [OpenConfig configuration file](/gnmi/test.json)
```
more ../gnmi/test.json 
```


## [gNMI](gnmi)

We will use gNMIc (an open source gNMI client)  
```
gnmic version
```

From the root of this repository: 
```
cd gnmi/ 
```

Lets use the following RPC: capabilities, get, subscribe, set.  

### gNMI capabilities
```
gnmic -a 172.28.135.38:6030 -u arista -p arista --insecure capabilities
```

### gNMI get 

Retrieve a snapshot for a path  

```
gnmic -a 172.28.135.38:6030 -u arista -p arista --insecure get --path  '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP]/bgp/neighbors'
gnmic -a 172.28.131.231:6030 -u arista -p arista --insecure get --path "/interfaces/interface[name=Ethernet3]/config/description"
```

### gNMI set 

The Set RPC is used to modify states.    

The SetRequest message uses the following fields:  
- "delete" field: A set of paths which are to be removed from the data tree  
- "replace" field: A set of "Update messages" indicating elements of the data tree whose content is to be replaced  
- "update" field: A set of "Update messages" indicating elements of the data tree whose content is to be updated  


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
### PyangBind + gNMI
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

### gNMI sub (to OpenConfig paths)

Request to the target to stream values for an OpenConfig path  

```
gnmic -a 172.28.135.38:6030 -u arista -p arista --insecure sub --path '/network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor[neighbor-address=::133:0:0:2]/state'
gnmic -a 172.28.135.38:6030 -u arista -p arista --insecure sub --path '/interfaces/interface[name=Ethernet1]/state/counters'
```
### gNMI sub (to EOS native paths)

Request to the target to stream values for an EOS native path  

```
gnmic -a 172.28.135.38:6030 -u arista -p arista --insecure sub --path "eos_native:/Sysdb/routing/bgp/export/"
```

### gNMI sub to ISIS LSDB

```
more gnmic_conf.yml
```
```
gnmic --config gnmic_conf.yml sub --path "eos_native:/Smash/routing/isis/lsdb/"
```
```
more gnmi_output.txt
```
Or
```
gnmic -a 172.28.135.38:6030 -u arista -p arista --insecure sub --path "eos_native:/Smash/routing/isis/lsdb/2/default/lsp" > redirect_output.txt
```
```
more redirect_output.txt
```


## Telegraf

Telegraf is an open source collector written in GO.  
Telegraf collects data and writes them into a database.  
It is plugin-driven (it has input plugins, output plugins, ...)  

Use this telegraf fork in order to have Telegraf to overwrite the gnmi timestamp by its local time  
more details https://gist.github.com/ksator/e36a1be086da6c2239c2c2c0eb9fe300  

From the root of this repository: 

```
git clone https://github.com/rski/telegraf
cd telegraf
make docker-image
docker images
```


## [TIG](TIG)  

A TIG stack uses:
   - Telegraf to collect data and to write the collected data in InfluxDB.
   - InfluxDB to store the data collected.
   - Grafana to visualize the data stored in InfluxDB.


### About the TIG stack setup 

From the root of this repository: 
```
cd TIG
```
```
more docker-compose.yml
ls telegraf.d/
ls dashboards
```

### Start the TIG stack 
```
docker-compose up -d
```
```
docker-compose ps
docker ps
docker images
```
### Check Telegraf logs
```
docker logs telegraf
```

### Query influxdb from CLI  

InfluxDB is an open source time series database written in GO.  

Start an interactive session

```
docker exec -it influxdb bash
```
```
influx
```
List databases
```
SHOW DATABASE
```
Select a database
```
use arista
```
List measurements
```
SHOW MEASUREMENTS
```
Query ifcounters measurement
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
Query openconfig_bgp measurement
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

### Query influxdb from python
```
pip3 freeze | grep influxdb
```
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

### Grafana GUI 

Grafana is an open source tool used to visualize time series data.  
It supports InfluxDB and other backends.  
It runs as a web application.  
It is written in GO.  

We can now use the Grafana GUI. 
The default username and password are admin/admin, but we changed them to arista/arista  
The datasource is already configured. It uses InfluxDB.  
We loaded ready to use dashboards.  

http://172.28.135.156:3000/login 

### Stop the TIG stack
```
docker-compose down
```
```
docker ps
```


