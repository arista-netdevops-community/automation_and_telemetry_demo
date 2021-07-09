This repository has Network automation demo and telemetry demo with EOS devices

**Table of content**
- [Set up an automation VM](#set-up-an-automation-vm)
- [Clone this repository](#clone-this-repository)
- [Configure EOS devices](#configure-eos-devices)
- [Netmiko](#netmiko)
- [eAPI (EOS API)](#eapi-eos-api)
- [Ansible](#ansible)
  - [Update the inventory](#update-the-inventory)
  - [Basic demo](#basic-demo)
  - [Collect `show commands` from the devices](#collect-show-commands-from-the-devices)
  - [Test the devices and generate a report](#test-the-devices-and-generate-a-report)
- [Pyang](#pyang)
  - [About Pyang](#about-pyang)
  - [Get YANG modules](#get-yang-modules)
    - [Clone the openconfig repository](#clone-the-openconfig-repository)
    - [Copy all the YANG files from OpenConfig to the yang_modules directory](#copy-all-the-yang-files-from-openconfig-to-the-yang_modules-directory)
    - [Move to the yang_modules directory](#move-to-the-yang_modules-directory)
  - [Validate YANG modules](#validate-yang-modules)
  - [Convert a YANG module into an equivalent YIN module](#convert-a-yang-module-into-an-equivalent-yin-module)
  - [Generate a tree representation of YANG modules for quick visualization](#generate-a-tree-representation-of-yang-modules-for-quick-visualization)
- [PyangBind](#pyangbind)
  - [About PyangBind](#about-pyangbind)
  - [Generate a Python module from a YANG module](#generate-a-python-module-from-a-yang-module)
  - [Use the new python module to generate OpenConfig configuration](#use-the-new-python-module-to-generate-openconfig-configuration)
- [gNMIc](#gnmic)
  - [gNMI Capabilities RPC](#gnmi-capabilities-rpc)
  - [gNMI Get RPC](#gnmi-get-rpc)
  - [gNMI Set RPC](#gnmi-set-rpc)
  - [gNMI Set RPC + PyangBind output](#gnmi-set-rpc--pyangbind-output)
  - [gNMI Subscribe RPC to OpenConfig paths](#gnmi-subscribe-rpc-to-openconfig-paths)
  - [gNMI Subscribe RPC to EOS native paths](#gnmi-subscribe-rpc-to-eos-native-paths)
  - [gNMI and EOS commands](#gnmi-and-eos-commands)
  - [gNMI configuration file](#gnmi-configuration-file)
  - [Generate the paths from a YANG file](#generate-the-paths-from-a-yang-file)
- [pyGNMI](#pygnmi)
  - [gNMI Capabilities RPC](#gnmi-capabilities-rpc-1)
  - [gNMI Get RPC](#gnmi-get-rpc-1)
  - [gNMI Subscribe RPC](#gnmi-subscribe-rpc)
  - [gNMI Set RPC](#gnmi-set-rpc-1)
    - [Update](#update)
    - [Delete](#delete)
- [TIG stack](#tig-stack)
  - [Telegraf plugins](#telegraf-plugins)
  - [Telegraf and gNMI timestamps](#telegraf-and-gnmi-timestamps)
  - [Check SNMP](#check-snmp)
  - [Update the required input for the TIG stack](#update-the-required-input-for-the-tig-stack)
  - [Start the TIG stack](#start-the-tig-stack)
  - [Check Telegraf logs](#check-telegraf-logs)
  - [Check Telegraf configuration](#check-telegraf-configuration)
  - [Query influxdb from CLI](#query-influxdb-from-cli)
  - [Query influxdb from python](#query-influxdb-from-python)
  - [Check Grafana](#check-grafana)
  - [Use Grafana GUI](#use-grafana-gui)
  - [Stop the TIG stack](#stop-the-tig-stack)

## Set up an automation VM

We are using this Ubuntu VM for this workshop:
```
$ lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 18.04.1 LTS
Release:        18.04
Codename:       bionic
```
Run these commands to update the VM and install tools
```
sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get install tree snmp python3-pip build-essential libssl-dev libffi-dev python3-dev -y
sudo apt install jq
pip3 install napalm netmiko jsonrpclib-pelix pyang pyangbind ansible==2.9.15 influxdb pygnmi
```
Check
```
pip3 list
```
```
$ python3 -V
Python 3.6.9
```
```
ansible --version
pyang --version
```

Then install also:
- docker (https://docs.docker.com/engine/install/ubuntu/)
- docker-compose (https://docs.docker.com/compose/install/)
- gnmic (https://gnmic.kmrd.dev./#installation)

Check
```
docker version
docker-compose version
gnmic version
```

## Clone this repository

Clone this repository

And then move to the local directory
```
cd automation_and_telemetry_demo
```

## Configure EOS devices

Configure all EOS devices for gNMI and SNMP and eAPI
```
snmp-server community public ro
snmp-server vrf MGMT
```
```
username arista secret 0 arista
```
```
management api gnmi
   transport grpc def
      vrf MGMT
   provider eos-native
```
```
management api http-commands
   protocol http
   no shutdown
```
and verify
```
DC1-LEAF1A#sho management http-server
SSL Profile:        none
FIPS Mode:          No
QoS DSCP:           0
Log Level:          none
CSP Frame Ancestor: None
TLS Protocols:      1.0 1.1 1.2
   VRF        Server Status      Enabled Services
---------- --------------------- ----------------
   MGMT       HTTPS: port 443    http-commands
```
```
DC1-LEAF1A#sho management api gnmi
Octa:               enabled
Enabled:            Yes
Server:             running on port 6030, in MGMT VRF
SSL Profile:        none
QoS DSCP:           none
```
no need to enable RESTCONF and NETCONF for this demo
```
DC1-LEAF1A#sho management api restconf
Enabled:            No
Server:             Not yet running
SSL Profile:        none
QoS DSCP:           none
```
```
DC1-LEAF1A#sho management api netconf
Enabled:            No
Server:             Not yet running
DC1-LEAF1A#
```
## Netmiko

Netmiko is a python library to simplify SSH connections to network devices.

So we can use it even when API is disabled on EOS devices (default). As example we can use it to enable API on EOS devices.

From the root of this repository, move to the [netmiko directory](netmiko)
```
cd netmiko
```
```
python3 collect_show_commands.py
more "show version.txt"
more "show ip interface brief.txt"
```
```
more config.txt
python3 configure_from_file.py
```

## eAPI (EOS API)

Once the API is enabled, the switch accepts HTTP(S) requests containing a list of EOS commands, and responds with machine-readable output serialized in JSON (served over HTTP or HTTPS).

From the root of this repository, move to the [eAPI directory](eapi)
```
cd eapi
```
```
python3 test1.py
python3 test2.py
```

## Ansible

We will use the ansible module [eos_command](https://docs.ansible.com/ansible/latest/collections/arista/eos/eos_command_module.html) and eAPI to run show commands on EOS devices.

From the root of the repository, move to the [Ansible directory](ansible)
```
cd ansible
```
### Update the inventory

Update the [inventory.yml](ansible/inventory.yml) file

Update the variables [group_vars](ansible/group_vars) and [host_vars](ansible/host_vars) directories

### Basic demo

```
ansible-playbook playbooks/print_version_and_models.yml
```
### Collect `show commands` from the devices

Update the list of `show commands` you want to collect (this is an ansible variable currently defined in the [group_vars](ansible/group_vars) directory) and execute this playbook:
```
ansible-playbook playbooks/snapshots.yml
```
The output of the `show commands` is saved in the directory [snaphots](ansible/snapshots)
```
tree snapshots
```
### Test the devices and generate a report

To run all the tests (NTP, LLDP, interfaces state, temperature, ...):
```
ansible-playbook playbooks/tests.yml
```
This will generate [this markdown report](ansible/reports/POC-state.md) and [this CSV report](ansible/reports/POC-state.csv)
```
ls reports
more reports/POC-state.md
more reports/POC-state.csv
```

To run all only some tests, use ansible tags.
Examples:
```
ansible-playbook playbooks/tests.yml --tags lldp
ansible-playbook playbooks/tests.yml --tags "hardware, ntp, reload_cause, arbgp"
```

## Pyang

### About Pyang

pyang is a python program.
We can use it to:
- Validate YANG modules against YANG RFCs
- Convert YANG modules into equivalent YIN module (XML)
- Generate a tree representation of YANG models for quick visualization

```
pip3 freeze | grep pyang
```
### Get YANG modules

We need YANG files.
#### Clone the openconfig repository

From the root of this repository:
```
git clone https://github.com/openconfig/public.git
```
```
ls public
```
#### Copy all the YANG files from OpenConfig to the yang_modules directory

```
cp public/release/models/*.yang yang_modules/.
cp -R public/release/models/*/*.yang yang_modules/.
cp public/third_party/ietf/*.yang yang_modules/.
```
#### Move to the yang_modules directory

It has all the YANG files published on the OpenConfig repository
```
cd yang_modules/
ls
```
### Validate YANG modules

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
pyang openconfig-interfaces.yang -f tree
pyang openconfig-interfaces.yang -f tree --tree-path=/interfaces/interface/state
pyang openconfig-interfaces.yang -f tree --tree-depth=4
```
```
pyang openconfig-bgp.yang -f tree --tree-path=/bgp/neighbors --tree-depth=4
pyang openconfig-bgp.yang -f tree --tree-path=/bgp/neighbors/neighbor/config
pyang openconfig-bgp.yang -f tree --tree-path=/bgp/neighbors/neighbor/state --tree-depth=5
pyang openconfig-bgp.yang -f tree --tree-path=/bgp/neighbors/neighbor/afi-safis --tree-depth=6
```
```
pyang openconfig-network-instance.yang -f tree --tree-depth=4
pyang openconfig-network-instance.yang -f tree  --tree-path=/network-instances/network-instance/protocols/protocol/bgp --tree-depth=6
pyang openconfig-network-instance.yang -f tree  --tree-path=/network-instances/network-instance/protocols/protocol/isis --tree-depth=6
```

## PyangBind

### About PyangBind

PyangBind is a pyang plugin.
It generates Python classes from a YANG module: It converts YANG module into a Python module, such that Python can be used to generate data which conforms with the data model defined in YANG.

```
pip3 freeze | grep pyang
```

From the root of this repository:
```
cd yang_modules/
```
### Generate a Python module from a YANG module

```
pyang --plugindir $HOME/.local/lib/python3.6/site-packages/pyangbind/plugin/ -f pybind -o oc_bgp.py openconfig-bgp.yang
```
The above command generated the python module oc_bgp.py from the openconfig-bgp.yang file
```
ls oc_bgp.py
```
### Use the new python module to generate OpenConfig configuration

The file [pyangbind_demo.py](yang_modules/pyangbind_demo.py) uses the new python module oc_bgp.py to generate this [OpenConfig configuration file](/gnmi/test.json)
```
more pyangbind_demo.py
python3 pyangbind_demo.py
```
```
more ../gnmi/test.json
```
This configuration will be loaded later on a switch using the [gNMI Set RPC](#gnmi-set-rpc--pyangbind-output)

## gNMIc

We will use gNMIc (an open source gNMI client)
```
gnmic version
```

From the root of this repository, move to the [gNMI directory](gnmi)
```
cd gnmi/
```

Lets use the following gNMI RPC: Capabilities, Get, Set, Subscribe.

### gNMI Capabilities RPC
```
gnmic -a 10.73.1.107:6030 -u arista -p arista --insecure capabilities
```

### gNMI Get RPC

Retrieve a snapshot for a path

```
gnmic -a 10.73.1.107:6030 -u arista -p arista --insecure get --path "/interfaces/interface[name=Ethernet2]/config/description"
gnmic -a 10.73.1.107:6030 -u arista -p arista --insecure get --path  "/interfaces/interface[name=Ethernet1]/config/enabled"
```

```
gnmic -a 10.73.1.107:6030 -u arista -p arista --insecure get --path  "/network-instances/network-instance[name=default]/protocols/protocol[name=BGP]/bgp"
gnmic -a 10.73.1.107:6030 -u arista -p arista --insecure get --path  '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP]/bgp/neighbors'
gnmic -a 10.73.1.107:6030 -u arista -p arista --insecure get --path "network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP]/bgp[afi-safi-name=IPV4_UNICAST]"
gnmic -a 10.73.1.107:6030 -u arista -p arista --insecure get --path  "network-instances/network-instance[name=default]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=172.31.255.8]/afi-safis/afi-safi"
```

### gNMI Set RPC

The Set RPC is used to modify states.

The SetRequest message uses the following fields:
- "delete" field: A set of paths which are to be removed from the data tree
- "replace" field: A set of "Update messages" indicating elements of the data tree whose content is to be replaced
- "update" field: A set of "Update messages" indicating elements of the data tree whose content is to be updated


```
gnmic -a 10.73.1.107:6030 --insecure -u arista -p arista get --path "/interfaces/interface[name=Ethernet1]/config/description"
gnmic -a 10.73.1.107:6030 --insecure -u arista -p arista set --update-path "/interfaces/interface[name=Ethernet1]/config/description" --update-value "gnmi-example"
gnmic -a 10.73.1.107:6030 --insecure -u arista -p arista get --path "/interfaces/interface[name=Ethernet1]/config/description"
sh run int et1
```
```
gnmic -a 10.73.1.107:6030 --insecure -u arista -p arista set --update  "/interfaces/interface[name=Ethernet3]/config/enabled:::bool:::false"
gnmic -a 10.73.1.107:6030 --insecure -u arista -p arista get --path  "/interfaces/interface[name=Ethernet3]/config/enabled"
sh run int et3
```
### gNMI Set RPC + PyangBind output
```
gnmic -a 10.73.1.117:6030 --insecure -u arista -p arista get --path '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP]/bgp'
```
```
sh run sec bgp
```
```
more test.json
```
```
gnmic -a 10.73.1.117:6030 --insecure -u arista -p arista set --replace-path '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP]/bgp' --replace-file test.json
gnmic -a 10.73.1.117:6030 --insecure -u arista -p arista get --path '/network-instances/network-instance[name=default]/protocols/protocol[name=BGP]/bgp'
```
```
sh run sec bgp
```
### gNMI Subscribe RPC to OpenConfig paths

Request to the target to stream values for an OpenConfig path

```
gnmic -a 10.73.1.107:6030 -u arista -p arista --insecure sub --path '/interfaces/interface[name=Ethernet1]/state/counters'
gnmic -a 10.73.1.107:6030 -u arista -p arista --insecure sub --path '/network-instances/network-instance/protocols/protocol/bgp/'
gnmic -a 10.73.1.107:6030 -u arista -p arista --insecure sub --path '/network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor[neighbor-address=::133:0:0:2]/state'
gnmic -a 10.73.1.107:6030 -u arista -p arista --insecure sub --path '/network-instances/network-instance[name=default]/protocols/protocol/bgp/neighbors/neighbor[neighbor-address=172.31.255.8]/state'
gnmic -a 10.73.1.107:6030 -u arista -p arista --insecure sub --path '/network-instances/network-instance[name=Tenant_B_WAN_Zone]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=10.255.254.5]/state'
```
```
gnmic -a 10.73.1.107:6030 -u arista -p arista --insecure sub --stream-mode "sample" --sample-interval "5s" --path '/network-instances/network-instance[name=default]/protocols/protocol/bgp/neighbors/neighbor[neighbor-address=172.31.255.8]/state'
```

### gNMI Subscribe RPC to EOS native paths

Request to the target to stream values for an EOS native path

```
gnmic -a 10.73.1.107:6030 -u arista -p arista --insecure sub --path "eos_native:/Sysdb/routing/bgp/export/"
```

### gNMI and EOS commands

Get an EOS show command via gNMI
```
gnmic -a 10.73.1.107:6030 -u arista -p arista --insecure get --path "cli:/show version"
```
```
gnmic -a 10.73.1.107:6030 -u arista -p arista --insecure  get --path "cli:/show ip route summary" | jq '.[0].updates[0].values."show ip route summary".totalRoutes'
```
The above RPC works if the device has this [YANG file](https://github.com/aristanetworks/yang/blob/master/EOS-4.24.2F/experimental/eos/models/arista-cli.yang)

You can check this using the Capabilities RPC:
```
gnmic -a 10.73.1.107:6030 -u arista -p arista --insecure capabilities | grep arista-cli
```
For more examples about EOS commands and gNMI you can refer to this [gist](https://gist.github.com/sulrich/81a2e2aec1d70d7a62f21a59299e640b)

### gNMI configuration file

```
ls -la
more .gnmic.yml
```
then
```
gnmic --config .gnmic.yml subscribe
```
or
```
gnmic subscribe
```
then
```
more gnmi_output.txt
```
### Generate the paths from a YANG file

```
cd ../yang_modules/
gnmic path --file openconfig-bgp.yang
gnmic path --file openconfig-bgp.yang | wc -l
gnmic path --file openconfig-bgp.yang --path-type gnmi
gnmic path --file openconfig-bgp.yang --types
```

## pyGNMI

pyGNMI is a Python implementation of the gNMI client

From the root of this repository, move to the [pygnmi directory](pygnmi)

```
cd pygnmi
```
### gNMI Capabilities RPC
```
python3 capabilities.py
```
### gNMI Get RPC
```
python3 get.py
```
### gNMI Subscribe RPC
```
python3 sub.py
```
### gNMI Set RPC
#### Update
```
python3 update.py
```
#### Delete
```
python3 delete.py
```

## TIG stack

Telegraf is an open source collector written in GO.
Telegraf collects data and writes them into a database.
It is plugin-driven (it has input plugins, output plugins, ...)

InfluxDB is an open source time series database written in GO.

Grafana is an open source tool used to visualize time series data.
It supports InfluxDB and other backends.
It runs as a web application.
It is written in GO.

A TIG stack uses:
   - Telegraf to collect data and to write the collected data in InfluxDB.
   - InfluxDB to store the data collected.
   - Grafana to visualize the data stored in InfluxDB

### Telegraf plugins

This Telegraf uses the following plugins:
- gnmi input plugin
- snmp input plugin
- Enum processor plugin
- influxdb output plugin
### Telegraf and gNMI timestamps

Use this telegraf fork in order to have Telegraf to overwrite the gnmi timestamp by its local time
more details https://gist.github.com/ksator/e36a1be086da6c2239c2c2c0eb9fe300

From the root of this repository:

```
git clone https://github.com/rski/telegraf
cd telegraf
make docker-image
docker images
```
### Check SNMP

We already tested gNMI.

Let's test SNMP:
```
snmpwalk --version
snmpwalk -v 2c -c public 10.73.1.107 .1.3.6.1.2.1.1.3.0
```

### Update the required input for the TIG stack

From the root of this repository, move to the [TIG](TIG) directory
```
cd TIG
```
Update the [input.yml](TIG/input.yml) with the devices details:
```
vi input.yml
```
Execute [this python script](TIG/render.py) to generate:
- the [docker-compose.yml file](TIG/docker-compose.yml) that starts/stops the TIG stack
- a Telegraf configuration file for each EOS device in the directory [telegraf.d](TIG/telegraf.d)
```
python3 render.py
more docker-compose.yml
ls telegraf.d/
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
### Check Telegraf configuration

```
docker exec -it telegraf bash
```
```
root@d35fed5663c0:/# ls /etc/telegraf
root@d35fed5663c0:/# more /etc/telegraf/telegraf.conf
root@d35fed5663c0:/# ls /etc/telegraf/telegraf.d
root@d35fed5663c0:/# exit
```

### Query influxdb from CLI

Start an interactive session

```
docker exec -it influxdb bash
```
```
influx
```
List databases
```
SHOW DATABASES
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
```
```
SHOW TAG VALUES FROM "ifcounters" with KEY = "device"
SHOW TAG VALUES FROM "ifcounters" with KEY = "name" WHERE ("device" = 'leaf1')
```
```
SELECT * FROM "ifcounters" WHERE "device" = 'leaf1'  ORDER BY DESC LIMIT 3
SELECT "in_octets","out_octets", "name" FROM "ifcounters" WHERE "device" = 'leaf1' ORDER BY DESC LIMIT 3
SELECT "in_octets","out_octets", "name" FROM "ifcounters" WHERE ("device" = 'leaf1' AND "name"='Ethernet2' AND time >= now() - 120s)
SELECT "in_octets","out_octets", "name" FROM "ifcounters" WHERE ("device" = 'leaf1' AND "name"=~/Ethernet.*/ AND time >= now() - 120s) GROUP BY "name"
SELECT mean("in_octets")*8 FROM "ifcounters" WHERE ("device" = 'leaf1' AND "name" = 'Ethernet2' AND time >= now() - 10m)
SELECT mean("in_octets")*8 FROM "ifcounters" WHERE ("device" = 'leaf1' AND "name" = 'Ethernet2' AND time >= now() - 10m) GROUP BY time(1m)
SELECT derivative(mean("in_octets"), 1s) *8 FROM "ifcounters" WHERE ("device" = 'leaf1' AND "name" = 'Ethernet2' AND time >= now() - 10m) GROUP BY time(1m)
SELECT derivative(mean("in_unicast_pkts"), 1s) FROM "ifcounters" WHERE ("device" = 'leaf1' AND "name" = 'Ethernet2') AND (time >= now() - 10m)  GROUP BY time(1m)
SELECT stddev("in_octets") FROM "ifcounters" WHERE ("device" = 'leaf1' AND ("name" = 'Ethernet1' OR "name" = 'Ethernet2') AND (time >= now() - 10m)) GROUP BY time(1m)
SELECT derivative(stddev("out_octets"), 1s)  / 8 FROM "ifcounters" WHERE ("device" =~ /lea.*/ AND "name" =~ /Ethernet[1|2]/ AND (time >= now() - 10m)) GROUP BY time(1m), "device"
```
Query openconfig_bgp measurement
```
SHOW TAG KEYS FROM "openconfig_bgp"
```
```
SHOW TAG VALUES FROM "openconfig_bgp" WITH KEY = "device"
SHOW TAG VALUES FROM "openconfig_bgp" WITH KEY = "name"
SHOW TAG VALUES FROM "openconfig_bgp" WITH KEY = "name" WHERE "device"='leaf1'
SHOW TAG VALUES FROM "openconfig_bgp" WITH KEY = "neighbor_address" WHERE "device"='leaf1'
SHOW TAG VALUES FROM "openconfig_bgp" WITH KEY = "neighbor_address" WHERE ("device"='leaf1' AND "name" = 'default')
```
```
SELECT LAST("neighbors/neighbor/state/session_state") FROM "openconfig_bgp" WHERE ("device"='leaf1' AND "neighbor_address" = '10.255.254.1')
SELECT LAST("neighbors/neighbor/state/session_state") FROM "openconfig_bgp" WHERE ("device"='leaf1') GROUP BY neighbor_address
SELECT LAST("neighbors/neighbor/state/session_state") FROM "openconfig_bgp" WHERE ("device"='leaf1' AND "name" = 'default') GROUP BY neighbor_address
SELECT LAST("neighbors/neighbor/state/session_state") AS session_state FROM "openconfig_bgp" WHERE "name" = 'default' GROUP BY "device", "neighbor_address"
SELECT "device", "neighbor_address", LAST("neighbors/neighbor/state/session_state") AS session_state FROM "openconfig_bgp" WHERE ("device"='leaf1' AND "neighbor_address" = '10.255.254.1')
```
```
SELECT "neighbors/neighbor/afi_safis/afi_safi/state/prefixes/received" FROM "openconfig_bgp" WHERE ("device" = 'leaf1' AND "neighbor_address"='10.255.254.1' AND "afi_safi_name"='IPV4_UNICAST')  LIMIT 15
SELECT mean("neighbors/neighbor/afi_safis/afi_safi/state/prefixes/sent") FROM "openconfig_bgp" WHERE ("device" = 'leaf1' AND "afi_safi_name" = 'IPV4_UNICAST' AND "name" = 'default') GROUP BY time(1m), "neighbor_address"
SELECT mean("neighbors/neighbor/afi_safis/afi_safi/state/prefixes/sent") FROM "openconfig_bgp" WHERE ("device" = 'leaf1' AND "name" = 'default') GROUP BY time(1m), "neighbor_address", "afi_safi_name"
```
```
SELECT mean("neighbors/neighbor/state/messages/sent/UPDATE") FROM "openconfig_bgp" WHERE ("device" = 'leaf1' AND "name" = 'default' AND time >= now() - 10m) GROUP BY "neighbor_address",time(1m)
```
```
SELECT COUNT(*) FROM (SELECT LAST("neighbors/neighbor/config/neighbor_address") FROM "openconfig_bgp" GROUP BY "neighbor_address") GROUP BY "device"
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
points = influx_client.query("""SELECT "in_octets" FROM "ifcounters" WHERE ("device"='leaf1' AND "name"='Ethernet1') ORDER BY DESC LIMIT 3""", database='arista').get_points()
for point in points:
     print(point['in_octets'])

exit()
```
### Check Grafana

The datasource is already configured. It uses InfluxDB.

We loaded ready to use dashboards.

We loaded a plugin.
```
docker exec -it grafana bash
```
```
bash-5.0$ more /etc/grafana/provisioning/datasources/datasource.yaml
bash-5.0$ more /etc/grafana/provisioning/dashboards/dashboards.yaml
bash-5.0$ ls /var/tmp/dashboards/
bash-5.0$ ls /var/lib/grafana/plugins
bash-5.0$ exit
```

### Use Grafana GUI

We can now use the Grafana GUI.
The default username and password are admin/admin, but we changed them to arista/arista.
The default port is 3000.

http://IP:3000/login

We can use the dashboards we already loaded or we can create new dashborads querying influxDB.
### Stop the TIG stack
```
docker-compose down
```
```
docker ps
```


