# ta366 Commands Output

## Table of Contents

- [show lldp neighbors](#show-lldp-neighbors)
- [show ip interface brief](#show-ip-interface-brief)
- [show interfaces description](#show-interfaces-description)
- [show version](#show-version)
## show interfaces description

```
Interface                      Status         Protocol           Description
Et1                            up             up                 
Et1.11                         up             up                 
Et1.12                         up             up                 
Et1.13                         up             up                 
Et1.14                         up             up                 
Et1.15                         up             up                 
Et1.25                         down           lowerlayerdown     
Et1.26                         up             up                 
Et2                            down           notpresent         
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
Et49/1                         up             up                 R2-E3/2/1
Et50/1                         up             up                 R5-E52/1
Et51/1                         up             up                 R6-E51/1
Et52/1                         down           down               
Et53/1                         down           notpresent         
Et54/1                         down           notpresent         
Lo1                            up             up                 
Lo2                            up             up                 
Lo3                            up             up                 
Lo4                            up             up                 
Ma1                            up             up
```
## show ip interface brief

```
Address 
Interface      IP Address          Status    Protocol             MTU   Owner   
-------------- ------------------- --------- ----------------- -------- ------- 
Ethernet1      unassigned          up        up                  1500           
Ethernet1.11   131.0.0.1/30        up        up                  1500           
Ethernet1.12   132.0.0.1/30        up        up                  1500           
Ethernet1.13   133.0.0.1/30        up        up                  1500           
Ethernet1.14   134.0.0.1/30        up        up                  1500           
Ethernet1.15   135.0.0.1/30        up        up                  1500           
Ethernet1.25   unassigned          down      lowerlayerdown         0           
Ethernet1.26   115.0.35.1/24       up        up                  1500           
Ethernet49/1   11.0.23.3/24        up        up                  9214           
Ethernet50/1   11.0.35.3/24        up        up                  9214           
Ethernet51/1   11.0.36.3/24        up        up                  9214           
Loopback1      25.0.1.3/32         up        up                 65535           
Loopback2      25.0.2.3/32         up        up                 65535           
Loopback3      25.0.3.3/32         up        up                 65535           
Loopback4      25.0.4.3/32         up        up                 65535           
Management1    172.28.135.38/20    up        up                  1500
```
## show lldp neighbors

```
Last table change time   : 1 day, 6:30:04 ago
Number of table inserts  : 73
Number of table deletes  : 69
Number of table drops    : 0
Number of table age-outs : 0

Port         Neighbor Device ID                          Neighbor Port ID   TTL 
---------- ------------------------------------------- -------------------- --- 
Et49/1       R2-cmp308.sjc.aristanetworks.com            Ethernet3/2/1      120 
Et50/1       R5-ta368.sjc.aristanetworks.com             Ethernet52/1       120 
Et51/1       R6-ta373.sjc.aristanetworks.com             Ethernet51/1       120 
Ma1          r161-rack3-tor42.sjc.aristanetworks.com     Ethernet15         120
```
## show version

```
Arista DCS-7280SR2K-48C6-M-F
Hardware version: 20.01
Serial number: JAS18070007
Hardware MAC address: 7483.ef73.55b3
System MAC address: 7483.ef73.55b3

Software image version: 4.25.1F
Architecture: i686
Internal build version: 4.25.1F-20001546.4251F
Internal build ID: 31358597-3f9d-49cf-b0a5-c16d16d21617

Uptime: 1 weeks, 2 days, 15 hours and 8 minutes
Total memory: 32822600 kB
Free memory: 28952596 kB
```
