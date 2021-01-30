# up522 Commands Output

## Table of Contents

- [show lldp neighbors](#show-lldp-neighbors)
- [show ip interface brief](#show-ip-interface-brief)
- [show interfaces description](#show-interfaces-description)
- [show version](#show-version)
- [show running-config](#show-running-config)
## show interfaces description

```
Interface                      Status         Protocol           Description
Et1/1                          up             up                 
Et2/1                          up             up                 
Et3/1                          up             up                 
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
Last table change time   : 2:21:50 ago
Number of table inserts  : 7
Number of table deletes  : 4
Number of table drops    : 0
Number of table age-outs : 0

Port        Neighbor Device ID                          Neighbor Port ID    TTL 
--------- ------------------------------------------- --------------------- --- 
Et2/1       ta368.sjc.aristanetworks.com                Ethernet2           120 
Et3/1       ta373.sjc.aristanetworks.com                Ethernet2           120 
Ma1         r161-rack3-tor42.sjc.aristanetworks.com     Ethernet11          120
```
## show running-config

```
! Command: show running-config
! device: up522 (DCS-7060CX-32S, EOS-4.25.1F-20348152.oslorel (engineering build))
!
! boot system flash:/oslo-rel-20349931.swi
!
prompt %H.%D{%H:%M:%S}%P
terminal length 0
alias ls bash ls -lrt /var/log/agents
alias senz show interface counter error | nz
alias shmc show int | awk '/^[A-Z]/ { intf = \$1 } /, address is/ { print intf, \$6 }'
alias snz show interface counter | nz
alias spd show port-channel %1 detail all
alias sqnz show interface counter queue | nz
alias srnz show interface counter rate | nz
!
daemon TerminAttr
   exec /usr/bin/TerminAttr -ingestgrpcurl=172.28.136.21:9910 -cvcompression=gzip -ingestauth=key,eossuper -smashexcludes=ale,flexCounter,hardware,kni,pulse,strata -ingestexclude=/Sysdb/cell/1/agent,/Sysdb/cell/2/agent -ingestvrf=default -taillogs
   no shutdown
!
vlan internal order ascending range 4020 4090
!
transceiver qsfp default-mode 4x10G
!
service routing protocols model ribd
!
logging format sequence-numbers
!
hostname up522
ip name-server vrf default 172.22.60.20
dns domain sjc.aristanetworks.com
!
ntp server 172.22.60.22
!
snmp-server community public ro
!
spanning-tree mode mstp
!
aaa authorization exec default local
!
aaa root secret sha512 $6$E67lCCdgLyoZHqUI$fpYmXZY58T2xOAi/oIUOIFWT/mf7/MLBTRWxPDIuuJAjzhYJgnJfw0EflRzfhpkI5I3/rYhn5oo8ypsu0te/m0
aaa authentication policy local allow-nopassword-remote-login
!
username admin privilege 15 role network-admin nopassword
username arista secret sha512 $6$oQa7L67OkJGS34Lp$N7y8.ZJVvjiMAU36v.RRlR10QBhnPUZHoKIistHIr411eU7Lc4J.O5QgVGk77DOqH8melynQfAC0iEj/ZFe7d0
username cvpadmin privilege 15 secret sha512 $6$VZQIOoRSDVGdF91/$3l4AQyO9kwEJJ4k.6JiG7AdFvQ7djVt70cGSjtB2jqroswgfsXkVtLrqQSAIeIJ/vpzbuyHbY3Pm1QC.0PXXk.
!
clock timezone PST8PDT
!
interface Ethernet1/1
!
interface Ethernet2/1
!
interface Ethernet3/1
!
interface Ethernet4/1
!
interface Ethernet5/1
!
interface Ethernet6/1
!
interface Ethernet7/1
!
interface Ethernet8/1
!
interface Ethernet9/1
!
interface Ethernet10/1
!
interface Ethernet11/1
!
interface Ethernet12/1
!
interface Ethernet13/1
!
interface Ethernet14/1
!
interface Ethernet15/1
!
interface Ethernet16/1
!
interface Ethernet17/1
!
interface Ethernet18/1
!
interface Ethernet19/1
!
interface Ethernet20/1
!
interface Ethernet21/1
!
interface Ethernet22/1
!
interface Ethernet23/1
!
interface Ethernet24/1
!
interface Ethernet25/1
!
interface Ethernet26/1
!
interface Ethernet27/1
!
interface Ethernet28/1
!
interface Ethernet29/1
!
interface Ethernet30/1
!
interface Ethernet31/1
!
interface Ethernet32/1
!
interface Ethernet33
!
interface Ethernet34
!
interface Management1
   ip address 172.28.132.154/20
!
ip access-list GNMI
   10 permit tcp any any eq gnmi
!
ip routing
!
ip route 10.80.0.0/12 172.28.128.1
ip route 10.240.0.0/14 172.28.128.1
ip route 172.16.0.0/12 172.28.128.1
!
management api http-commands
   protocol http
   no shutdown
!
management api gnmi
   transport grpc def
      ip access-group GNMI
   provider eos-native
!
end
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

Uptime: 1 weeks, 1 days, 19 hours and 29 minutes
Total memory: 8099060 kB
Free memory: 6203964 kB
```
