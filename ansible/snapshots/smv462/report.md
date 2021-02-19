# smv462 Commands Output

## Table of Contents

- [show lldp neighbors](#show-lldp-neighbors)
- [show ip interface brief](#show-ip-interface-brief)
- [show interfaces description](#show-interfaces-description)
- [show version](#show-version)
## show interfaces description

```
Interface                      Status         Protocol           Description
Et1/1                          up             up                 R2-E3/1/1
Et2/1                          up             up                 R4-E49/1
Et3/1                          up             up                 R5-E50/1
Et4/1                          down           notpresent         
Et5/1                          down           notpresent         
Et6/1                          down           notpresent         
Et7/1                          down           notpresent         
Et8/1                          down           notpresent         
Et9/1                          up             up                 
Et11/1                         up             up                 
Et11/1.1                       down           lowerlayerdown     
Et11/1.11                      up             up                 
Et11/1.12                      up             up                 
Et11/1.13                      up             up                 
Et11/1.14                      up             up                 
Et11/1.15                      up             up                 
Et11/1.100                     up             up                 
Et13/1                         down           notpresent         
Et14/1                         down           notpresent         
Et15/1                         down           notpresent         
Et16/1                         down           notpresent         
Et17/1                         down           notpresent         
Et18/1                         down           notpresent         
Et19/1                         down           notpresent         
Et20/1                         down           notpresent         
Et21/1                         down           notpresent         
Et22/1                         down           notpresent         
Et23/1                         down           notpresent         
Et24/1                         down           notpresent         
Et25/1                         down           notpresent         
Et26/1                         down           notpresent         
Et27/1                         down           notpresent         
Et28/1                         down           notpresent         
Et29/1                         down           notpresent         
Et30/1                         down           notpresent         
Et31/1                         down           notpresent         
Et32/1                         down           notpresent         
Et33/1                         down           notpresent         
Et34/1                         down           notpresent         
Et35/1                         down           notpresent         
Et36/1                         down           notpresent         
Lo1                            up             up                 
Lo2                            up             up                 
Lo3                            up             up                 
Ma1                            up             up
```
## show ip interface brief

```
Address 
Interface         IP Address          Status   Protocol            MTU  Owner   
----------------- ------------------- -------- ---------------- ------- ------- 
Ethernet1/1       11.0.12.1/24        up       up                 9214          
Ethernet2/1       11.0.14.1/24        up       up                 9214          
Ethernet3/1       11.0.15.1/24        up       up                 9214          
Ethernet9/1       102.1.0.1/24        up       up                 9214          
Ethernet11/1      unassigned          up       up                 1500          
Ethernet11/1.1    unassigned          down     lowerlayerdown        0          
Ethernet11/1.11   111.0.0.1/30        up       up                 1500          
Ethernet11/1.12   112.0.0.1/30        up       up                 1500          
Ethernet11/1.13   113.0.0.1/30        up       up                 1500          
Ethernet11/1.14   114.0.0.1/30        up       up                 1500          
Ethernet11/1.15   115.0.0.1/30        up       up                 1500          
Ethernet11/1.100  101.1.0.1/24        up       up                    0          
Loopback1         25.0.1.1/32         up       up                65535          
Loopback2         25.0.2.1/32         up       up                65535          
Loopback3         unassigned          up       up                65535          
Management1       172.28.134.246/20   up       up                 1500
```
## show lldp neighbors

```
Last table change time   : 0:44:10 ago
Number of table inserts  : 83
Number of table deletes  : 79
Number of table drops    : 0
Number of table age-outs : 0

Port        Neighbor Device ID                          Neighbor Port ID    TTL 
--------- ------------------------------------------- --------------------- --- 
Et1/1       R2-cmp308.sjc.aristanetworks.com            Ethernet3/1/1       120 
Et2/1       R4-ta367.sjc.aristanetworks.com             Ethernet49/1        120 
Et3/1       R5-ta368.sjc.aristanetworks.com             Ethernet50/1        120 
Ma1         r161-rack3-tor42.sjc.aristanetworks.com     Ethernet17          120
```
## show version

```
Arista DCS-7280CR3K-32P4-F
Hardware version: 11.00
Serial number: JPE19362870
Hardware MAC address: fcbd.673c.0ec1
System MAC address: fcbd.673c.0ec1

Software image version: 4.25.2F
Architecture: i686
Internal build version: 4.25.2F-20711308.4252F
Internal build ID: d314b2cb-9b28-4b3b-a39c-7d8238d8602d

Uptime: 0 weeks, 3 days, 0 hours and 23 minutes
Total memory: 65850612 kB
Free memory: 61442648 kB
```
