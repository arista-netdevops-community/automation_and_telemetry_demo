# DC1-LEAF1A Commands Output

## Table of Contents

- [show lldp neighbors](#show-lldp-neighbors)
- [show ip interface brief](#show-ip-interface-brief)
- [show interfaces description](#show-interfaces-description)
- [show version](#show-version)
## show interfaces description

```
Interface                      Status         Protocol           Description
Et1                            up             up                 P2P_LINK_TO_DC1-SPINE1_Ethernet1
Et2                            up             up                 P2P_LINK_TO_DC1-SPINE2_Ethernet1
Et3                            up             up                 DC1-L2LEAF1A_Ethernet1
Et4                            up             up                 DC1-L2LEAF2A_Ethernet1
Et5                            up             up                 server01_Eth0
Et6                            up             up                 server03_Eth0
Et7                            up             up                 MLAG_PEER_DC1-LEAF1B_Ethernet7
Et8                            up             up                 MLAG_PEER_DC1-LEAF1B_Ethernet8
Lo0                            up             up                 EVPN_Overlay_Peering
Lo1                            up             up                 VTEP_VXLAN_Tunnel_Source
Ma1                            up             up                 oob_management
Po3                            up             up                 DC1_L2LEAF1_Po1
Po4                            up             up                 DC1_L2LEAF2_Po1
Po6                            down           lowerlayerdown     server03_server03
Po7                            up             up                 MLAG_PEER_DC1-LEAF1B_Po7
Vl110                          up             up                 Tenant_A_APP_Zone_2
Vl111                          up             up                 Tenant_A_APP_Zone_3
Vl112                          up             up                 Tenant_A_APP_Zone_1
Vl120                          up             up                 Tenant_A_WEB_Zone_1
Vl121                          up             up                 Tenant_A_WEB_Zone_2
Vl210                          up             up                 Tenant_B_APP_Zone_1
Vl211                          up             up                 Tenant_B_APP_Zone_2
Vl250                          up             up                 Tenant_B_WAN_Zone_1
Vl1156                         up             up                 
Vl1157                         up             up                 
Vl1196                         up             up                 
Vl1198                         up             up                 
Vl3009                         up             up                 MLAG_PEER_L3_iBGP: vrf Tenant_A_APP_Zone
Vl3010                         up             up                 MLAG_PEER_L3_iBGP: vrf Tenant_A_WEB_Zone
Vl3019                         up             up                 MLAG_PEER_L3_iBGP: vrf Tenant_B_APP_Zone
Vl3020                         up             up                 MLAG_PEER_L3_iBGP: vrf Tenant_B_WAN_Zone
Vl4093                         up             up                 MLAG_PEER_L3_PEERING
Vl4094                         up             up                 MLAG_PEER
Vx1                            up             up
```
## show ip interface brief

```
Address 
Interface       IP Address           Status     Protocol         MTU    Owner   
--------------- -------------------- ---------- ------------ ---------- ------- 
Ethernet1       172.31.255.1/31      up         up              1500            
Ethernet2       172.31.255.3/31      up         up              1500            
Loopback0       192.168.255.3/32     up         up             65535            
Loopback1       192.168.254.3/32     up         up             65535            
Management1     10.73.1.105/24       up         up              1500            
Vlan110         10.1.110.1/24        up         up              1500            
Vlan111         10.1.111.1/24        up         up              1500            
Vlan112         10.1.112.1/24        up         up              1500            
Vlan120         10.1.120.1/24        up         up              1500            
Vlan121         10.1.121.1/24        up         up              1500            
Vlan210         10.2.210.1/24        up         up              1500            
Vlan211         10.2.211.1/24        up         up              1500            
Vlan250         10.2.250.1/24        up         up              1500            
Vlan1156        unassigned           up         up              9164            
Vlan1157        unassigned           up         up              9164            
Vlan1196        unassigned           up         up              9164            
Vlan1198        unassigned           up         up              9164            
Vlan3009        10.255.254.0/31      up         up              1500            
Vlan3010        10.255.254.0/31      up         up              1500            
Vlan3019        10.255.254.0/31      up         up              1500            
Vlan3020        10.255.254.0/31      up         up              1500            
Vlan4093        10.255.254.0/31      up         up              1500            
Vlan4094        10.255.252.0/31      up         up              1500
```
## show lldp neighbors

```
Last table change time   : 27 days, 3:59:25 ago
Number of table inserts  : 20
Number of table deletes  : 7
Number of table drops    : 0
Number of table age-outs : 6

Port          Neighbor Device ID            Neighbor Port ID    TTL 
---------- ----------------------------- ---------------------- --- 
Et1           DC1-SPINE1.arista.com         Ethernet1           120 
Et2           DC1-SPINE2.arista.com         Ethernet1           120 
Et3           DC1-L2LEAF1A.arista.com       Ethernet1           120 
Et4           DC1-L2LEAF2A.arista.com       Ethernet1           120 
Et7           DC1-LEAF1B.arista.com         Ethernet7           120 
Et8           DC1-LEAF1B.arista.com         Ethernet8           120 
Ma1           DC1-LEAF2A.arista.com         Management1         120 
Ma1           DC1-LEAF1B.arista.com         Management1         120 
Ma1           DC1-LEAF2B.arista.com         Management1         120 
Ma1           DC1-L2LEAF1A.arista.com       Management1         120 
Ma1           DC1-L2LEAF2A.arista.com       Management1         120 
Ma1           DC1-SPINE2.arista.com         Management1         120 
Ma1           DC1-SPINE1.arista.com         Management1         120
```
## show version

```
vEOS
Hardware version:    
Serial number:       
System MAC address:  5014.000d.6f23

Software image version: 4.24.0F
Architecture:           i686
Internal build version: 4.24.0F-16270098.4240F
Internal build ID:      da8d6269-c25f-4a12-930b-c3c42c12c38a

Uptime:                 6 weeks, 4 days, 6 hours and 43 minutes
Total memory:           4008604 kB
Free memory:            2723108 kB
```
