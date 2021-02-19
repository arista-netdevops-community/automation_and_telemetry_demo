# ta373 Commands Output

## Table of Contents

- [show lldp neighbors](#show-lldp-neighbors)
- [show ip interface brief](#show-ip-interface-brief)
- [show interfaces description](#show-interfaces-description)
- [show version](#show-version)
## show interfaces description

```
Interface                      Status         Protocol           Description
Et1                            up             up                 
Et1.16                         up             up                 
Et1.17                         up             up                 
Et1.18                         up             up                 
Et1.19                         up             up                 
Et1.25                         up             up                 
Et1.26                         up             up                 
Et2                            up             up                 
Et3                            down           notpresent         
Et4                            down           notpresent         
Et5                            down           notpresent         
Et6                            down           notpresent         
Et7                            down           notpresent         
Et8                            down           notpresent         
Et9                            down           notpresent         
Et10                           down           notpresent         
Et11                           down           notpresent         
Et12                           down           notpresent         
Et13                           down           notpresent         
Et14                           down           notpresent         
Et15                           down           notpresent         
Et16                           down           notpresent         
Et17                           down           notpresent         
Et18                           down           notpresent         
Et19                           down           notpresent         
Et20                           down           notpresent         
Et21                           down           notpresent         
Et22                           down           notpresent         
Et23                           down           notpresent         
Et24                           down           notpresent         
Et25                           down           notpresent         
Et26                           down           notpresent         
Et27                           down           notpresent         
Et28                           down           notpresent         
Et29                           down           notpresent         
Et30                           down           notpresent         
Et31                           down           notpresent         
Et32                           down           notpresent         
Et33                           down           notpresent         
Et34                           down           notpresent         
Et35                           down           notpresent         
Et36                           down           notpresent         
Et37                           down           notpresent         
Et38                           down           notpresent         
Et39                           down           notpresent         
Et40                           down           notpresent         
Et41                           down           notpresent         
Et42                           down           notpresent         
Et43                           down           notpresent         
Et44                           down           notpresent         
Et45                           down           notpresent         
Et46                           down           notpresent         
Et47                           down           notpresent         
Et48                           down           notpresent         
Et49/1                         up             up                 R5-E53/1
Et50/1                         up             up                 R2-E3/5/1
Et51/1                         up             up                 R3-E51/1
Et52/1                         down           notpresent         
Et53/1                         down           notpresent         
Et54/1                         down           notpresent         
Lo1                            up             up                 
Lo2                            up             up                 
Lo3                            up             up                 
Lo4                            up             up                 
Ma1                            up             up                 
Vl20                           up             up                 
Vl21                           up             up                 
Vl22                           up             up                 
Vl23                           up             up
```
## show ip interface brief

```
Address 
Interface        IP Address           Status     Protocol         MTU   Owner   
---------------- -------------------- ---------- ------------ --------- ------- 
Ethernet1        unassigned           up         up              9000           
Ethernet1.16     unassigned           up         up              9000           
Ethernet1.17     unassigned           up         up              9000           
Ethernet1.18     unassigned           up         up              9000           
Ethernet1.19     unassigned           up         up              9000           
Ethernet1.25     125.25.25.1/24       up         up              9000           
Ethernet1.26     115.0.15.1/24        up         up              9000           
Ethernet49/1     11.0.56.6/24         up         up              9214           
Ethernet50/1     11.0.26.6/24         up         up              9214           
Ethernet51/1     11.0.36.6/24         up         up              9214           
Loopback1        25.0.1.6/32          up         up             65535           
Loopback2        25.0.2.6/32          up         up             65535           
Loopback3        25.0.3.6/32          up         up             65535           
Loopback4        25.0.4.6/32          up         up             65535           
Management1      172.28.134.80/20     up         up              1500           
Vlan20           unassigned           up         up              1500           
Vlan21           unassigned           up         up              1500           
Vlan22           25.0.0.253/24        up         up              1500           
Vlan23           23.0.0.253/24        up         up              1500
```
## show lldp neighbors

```
Last table change time   : 3:31:14 ago
Number of table inserts  : 35
Number of table deletes  : 30
Number of table drops    : 0
Number of table age-outs : 0

Port         Neighbor Device ID                          Neighbor Port ID   TTL 
---------- ------------------------------------------- -------------------- --- 
Et2          up522.sjc.aristanetworks.com                Ethernet3/1        120 
Et49/1       R5-ta368.sjc.aristanetworks.com             Ethernet53/1       120 
Et50/1       R2-cmp308.sjc.aristanetworks.com            Ethernet3/5/1      120 
Et51/1       R3-ta366.sjc.aristanetworks.com             Ethernet51/1       120 
Ma1          r161-rack3-tor42.sjc.aristanetworks.com     Ethernet12         120
```
## show version

```
Arista DCS-7280SR2K-48C6-M-F
Hardware version: 21.01
Serial number: JPE18271569
Hardware MAC address: 7483.ef95.e588
System MAC address: 7483.ef95.e588

Software image version: 4.25.1F
Architecture: i686
Internal build version: 4.25.1F-20001546.4251F
Internal build ID: 31358597-3f9d-49cf-b0a5-c16d16d21617

Uptime: 1 weeks, 2 days, 15 hours and 8 minutes
Total memory: 32822600 kB
Free memory: 29065212 kB
```
