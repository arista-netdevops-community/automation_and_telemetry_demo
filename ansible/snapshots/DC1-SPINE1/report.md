# DC1-SPINE1 Commands Output

## Table of Contents

- [show lldp neighbors](#show-lldp-neighbors)
- [show ip interface brief](#show-ip-interface-brief)
- [show interfaces description](#show-interfaces-description)
- [show version](#show-version)
## show interfaces description

```
Interface                      Status         Protocol           Description
Et1                            up             up                 P2P_LINK_TO_DC1-LEAF1A_Ethernet1
Et2                            up             up                 P2P_LINK_TO_DC1-LEAF1B_Ethernet1
Et3                            up             up                 
Et4                            up             up                 P2P_LINK_TO_DC1-LEAF2A_Ethernet1
Et5                            up             up                 P2P_LINK_TO_DC1-LEAF2B_Ethernet1
Et6                            up             up                 
Et7                            up             up                 
Et8                            up             up                 
Lo0                            up             up                 EVPN_Overlay_Peering
Ma1                            up             up                 oob_management
```
## show ip interface brief

```
Address 
Interface       IP Address           Status     Protocol         MTU    Owner   
--------------- -------------------- ---------- ------------ ---------- ------- 
Ethernet1       172.31.255.0/31      up         up              1500            
Ethernet2       172.31.255.4/31      up         up              1500            
Ethernet4       172.31.255.8/31      up         up              1500            
Ethernet5       172.31.255.12/31     up         up              1500            
Loopback0       192.168.255.1/32     up         up             65535            
Management1     10.73.1.101/24       up         up              1500
```
## show lldp neighbors

```
Last table change time   : 27 days, 3:59:25 ago
Number of table inserts  : 14
Number of table deletes  : 2
Number of table drops    : 0
Number of table age-outs : 0

Port          Neighbor Device ID            Neighbor Port ID    TTL 
---------- ----------------------------- ---------------------- --- 
Et1           DC1-LEAF1A.arista.com         Ethernet1           120 
Et2           DC1-LEAF1B.arista.com         Ethernet1           120 
Et4           DC1-LEAF2A.arista.com         Ethernet1           120 
Et5           DC1-LEAF2B.arista.com         Ethernet1           120 
Et7           DC1-SPINE2.arista.com         Ethernet7           120 
Ma1           DC1-L2LEAF1A.arista.com       Management1         120 
Ma1           DC1-SPINE2.arista.com         Management1         120 
Ma1           DC1-LEAF1B.arista.com         Management1         120 
Ma1           DC1-LEAF2A.arista.com         Management1         120 
Ma1           DC1-LEAF2B.arista.com         Management1         120 
Ma1           DC1-L2LEAF2A.arista.com       Management1         120 
Ma1           DC1-LEAF1A.arista.com         Management1         120
```
## show version

```
vEOS
Hardware version:    
Serial number:       
System MAC address:  0c1d.c0a3.86f3

Software image version: 4.24.0F
Architecture:           i686
Internal build version: 4.24.0F-16270098.4240F
Internal build ID:      da8d6269-c25f-4a12-930b-c3c42c12c38a

Uptime:                 5 weeks, 0 days, 5 hours and 36 minutes
Total memory:           4008604 kB
Free memory:            2958020 kB
```
