# DC1-SPINE2 Commands Output

## Table of Contents

- [show lldp neighbors](#show-lldp-neighbors)
- [show ip interface brief](#show-ip-interface-brief)
- [show interfaces description](#show-interfaces-description)
- [show version](#show-version)
## show interfaces description

```
Interface                      Status         Protocol           Description
Et1                            up             up                 P2P_LINK_TO_DC1-LEAF1A_Ethernet2
Et2                            up             up                 P2P_LINK_TO_DC1-LEAF1B_Ethernet2
Et3                            up             up                 
Et4                            up             up                 P2P_LINK_TO_DC1-LEAF2A_Ethernet2
Et5                            up             up                 P2P_LINK_TO_DC1-LEAF2B_Ethernet2
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
Ethernet1       172.31.255.2/31      up         up              1500            
Ethernet2       172.31.255.6/31      up         up              1500            
Ethernet4       172.31.255.10/31     up         up              1500            
Ethernet5       172.31.255.14/31     up         up              1500            
Loopback0       192.168.255.2/32     up         up             65535            
Management1     10.73.1.102/24       up         up              1500
```
## show lldp neighbors

```
Last table change time   : 35 days, 4:14:59 ago
Number of table inserts  : 13
Number of table deletes  : 1
Number of table drops    : 0
Number of table age-outs : 0

Port          Neighbor Device ID            Neighbor Port ID    TTL 
---------- ----------------------------- ---------------------- --- 
Et1           DC1-LEAF1A.arista.com         Ethernet2           120 
Et2           DC1-LEAF1B.arista.com         Ethernet2           120 
Et4           DC1-LEAF2A.arista.com         Ethernet2           120 
Et5           DC1-LEAF2B.arista.com         Ethernet2           120 
Et7           DC1-SPINE1.arista.com         Ethernet7           120 
Ma1           DC1-LEAF2A.arista.com         Management1         120 
Ma1           DC1-LEAF2B.arista.com         Management1         120 
Ma1           DC1-LEAF1B.arista.com         Management1         120 
Ma1           DC1-LEAF1A.arista.com         Management1         120 
Ma1           DC1-L2LEAF1A.arista.com       Management1         120 
Ma1           DC1-L2LEAF2A.arista.com       Management1         120 
Ma1           DC1-SPINE1.arista.com         Management1         120
```
## show version

```
vEOS
Hardware version:    
Serial number:       
System MAC address:  5014.0034.236a

Software image version: 4.24.0F
Architecture:           i686
Internal build version: 4.24.0F-16270098.4240F
Internal build ID:      da8d6269-c25f-4a12-930b-c3c42c12c38a

Uptime:                 5 weeks, 0 days, 5 hours and 36 minutes
Total memory:           4008604 kB
Free memory:            2960620 kB
```
