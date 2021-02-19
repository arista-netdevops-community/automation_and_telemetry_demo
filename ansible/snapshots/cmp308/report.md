# cmp308 Commands Output

## Table of Contents

- [show lldp neighbors](#show-lldp-neighbors)
- [show ip interface brief](#show-ip-interface-brief)
- [show interfaces description](#show-interfaces-description)
- [show version](#show-version)
## show interfaces description

```
Interface                      Status         Protocol           Description
Et3/1/1                        up             up                 R1-E1/1
Et3/2/1                        up             up                 R3-E49/1
Et3/3/1                        admin down     down               R4-E50/1
Et3/4/1                        up             up                 R5-E51/1
Et3/5/1                        up             up                 R6-E50/1
Et3/6/1                        admin down     down               
Et3/7/1                        down           notpresent         
Et3/8/1                        down           notpresent         
Et3/10/1                       up             up                 
Et3/10/1.11                    up             up                 
Et3/10/1.12                    up             up                 
Et3/10/1.13                    up             up                 
Et3/10/1.14                    up             up                 
Et3/10/1.15                    up             up                 
Et3/11/1                       down           notpresent         
Et3/12/1                       down           notpresent         
Et3/13/1                       down           notpresent         
Et3/14/1                       down           notpresent         
Et3/15/1                       down           notpresent         
Et3/16/1                       down           notpresent         
Et3/17/1                       down           notpresent         
Et3/18/1                       down           notpresent         
Et3/19/1                       down           notpresent         
Et3/20/1                       down           notpresent         
Et3/21/1                       down           notpresent         
Et3/22/1                       down           notpresent         
Et3/23/1                       down           notpresent         
Et3/24/1                       down           notpresent         
Et3/25/1                       down           notpresent         
Et3/26/1                       down           notpresent         
Et3/27/1                       down           notpresent         
Et3/28/1                       down           notpresent         
Et3/29/1                       down           notpresent         
Et3/30/1                       down           notpresent         
Et3/31/1                       down           notpresent         
Et3/32/1                       down           notpresent         
Et3/33/1                       down           notpresent         
Et3/34/1                       down           notpresent         
Et3/35/1                       down           notpresent         
Et3/36/1                       down           notpresent         
Et3/37/1                       down           notpresent         
Et3/38/1                       down           notpresent         
Et3/39/1                       down           notpresent         
Et3/40/1                       down           notpresent         
Et3/41/1                       down           notpresent         
Et3/42/1                       down           notpresent         
Et3/43/1                       down           notpresent         
Et3/44/1                       down           notpresent         
Et3/45/1                       down           notpresent         
Et3/46/1                       down           notpresent         
Et3/47/1                       down           notpresent         
Et3/48/1                       down           notpresent         
Lo1                            up             up                 
Lo2                            up             up                 
Ma1/1                          up             up                 
Ma1/2                          down           down
```
## show ip interface brief

```
Address 
Interface           IP Address          Status       Protocol      MTU  Owner   
------------------- ------------------- ------------ ---------- ------- ------- 
Ethernet3/1/1       11.0.12.2/24        up           up           9214          
Ethernet3/2/1       11.0.23.2/24        up           up           9214          
Ethernet3/3/1       11.0.24.2/24        admin down   down         9214          
Ethernet3/4/1       11.0.25.2/24        up           up           9214          
Ethernet3/5/1       11.0.26.2/24        up           up           9214          
Ethernet3/10/1      unassigned          up           up           1500          
Ethernet3/10/1.11   121.0.0.1/30        up           up           1500          
Ethernet3/10/1.12   122.0.0.1/30        up           up           1500          
Ethernet3/10/1.13   123.0.0.1/30        up           up           1500          
Ethernet3/10/1.14   124.0.0.1/30        up           up           1500          
Ethernet3/10/1.15   125.0.0.1/30        up           up           1500          
Loopback1           25.0.1.2/32         up           up          65535          
Loopback2           25.0.2.2/32         up           up          65535          
Management1/1       172.28.135.145/20   up           up           1500          
Management1/2       unassigned          down         down         1500
```
## show lldp neighbors

```
Last table change time   : 1 day, 6:12:06 ago
Number of table inserts  : 305
Number of table deletes  : 300
Number of table drops    : 0
Number of table age-outs : 0

Port         Neighbor Device ID                          Neighbor Port ID   TTL 
---------- ------------------------------------------- -------------------- --- 
Et3/1/1      R1-smv462.sjc.aristanetworks.com            Ethernet1/1        120 
Et3/2/1      R3-ta366.sjc.aristanetworks.com             Ethernet49/1       120 
Et3/4/1      R5-ta368.sjc.aristanetworks.com             Ethernet51/1       120 
Et3/5/1      R6-ta373.sjc.aristanetworks.com             Ethernet50/1       120 
Ma1/1        r161-rack3-tor42.sjc.aristanetworks.com     Ethernet10         120
```
## show version

```
Arista DCS-7804-CH
Hardware version: 11.02
Serial number: TMO20410350
Hardware MAC address: 985d.82ff.fea8
System MAC address: 985d.82ff.fea8

Software image version: 4.25.1F
Architecture: i686
Internal build version: 4.25.1F-20001546.4251F
Internal build ID: 31358597-3f9d-49cf-b0a5-c16d16d21617

Uptime: 1 weeks, 2 days, 15 hours and 10 minutes
Total memory: 65869424 kB
Free memory: 59900564 kB
```
