# up522 Commands Output

## Table of Contents

- [show lldp neighbors](#show-lldp-neighbors)
- [show ip interface brief](#show-ip-interface-brief)
- [show interfaces description](#show-interfaces-description)
- [show version](#show-version)
## show interfaces description

```
Interface                      Status         Protocol           Description
Et1/1                          up             up                 r161-rack4-ixia1-2/8
Et2/1                          up             up                 ta368_et2
Et3/1                          up             up                 ta373_et2
Et4/1                          down           notpresent         
Et5/1                          down           notpresent         
Et6/1                          down           notpresent         
Et7/1                          down           notpresent         
Et8/1                          down           notpresent         
Et9/1                          down           notpresent         
Et10/1                         down           notpresent         
Et11/1                         down           notpresent         
Et12/1                         down           notpresent         
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
Et33                           down           notpresent         
Et34                           down           notpresent         
Ma1                            up             up                 
Po2100                         down           lowerlayerdown
```
## show ip interface brief

```
Address 
Interface       IP Address            Status     Protocol        MTU    Owner   
--------------- --------------------- ---------- ------------ --------- ------- 
Management1     172.28.132.154/20     up         up             1500
```
## show lldp neighbors

```
Last table change time   : 3:32:00 ago
Number of table inserts  : 34
Number of table deletes  : 31
Number of table drops    : 0
Number of table age-outs : 0

Port        Neighbor Device ID                          Neighbor Port ID    TTL 
--------- ------------------------------------------- --------------------- --- 
Et2/1       R5-ta368.sjc.aristanetworks.com             Ethernet2           120 
Et3/1       R6-ta373.sjc.aristanetworks.com             Ethernet2           120 
Ma1         r161-rack3-tor42.sjc.aristanetworks.com     Ethernet11          120
```
## show version

```
Arista DCS-7060CX-32S-F
Hardware version: 12.00
Serial number: JPE16491240
Hardware MAC address: 2899.3a15.22b9
System MAC address: 2899.3a15.22b9

Software image version: 4.25.1F-20348152.oslorel (engineering build)
Architecture: i686
Internal build version: 4.25.1F-20348152.oslorel
Internal build ID: 21839e6b-0fd0-4fdc-86f1-919012c49df3

Uptime: 2 weeks, 2 days, 17 hours and 37 minutes
Total memory: 8099060 kB
Free memory: 6158180 kB
```
