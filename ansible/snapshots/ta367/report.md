# ta367 Commands Output

## Table of Contents

- [show lldp neighbors](#show-lldp-neighbors)
- [show ip interface brief](#show-ip-interface-brief)
- [show interfaces description](#show-interfaces-description)
- [show version](#show-version)
- [show running-config](#show-running-config)
## show interfaces description

```
Interface                      Status         Protocol           Description
Et1                            up             up                 
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
Et49/1                         up             up                 R1-E2/1
Et50/1                         up             up                 R2-E3/3/1
Et51/1                         up             up                 R5-E49/1
Et52/1                         down           notpresent         
Et53/1                         down           notpresent         
Et54/1                         down           notpresent         
Lo1                            up             up                 
Lo2                            up             up                 
Ma1                            up             up                 
Vl100                          up             up                 
Vl300                          up             up
```
## show ip interface brief

```
Address 
Interface        IP Address           Status     Protocol         MTU   Owner   
---------------- -------------------- ---------- ------------ --------- ------- 
Ethernet49/1     11.0.14.4/24         up         up              9214           
Ethernet50/1     11.0.24.4/24         up         up              9214           
Ethernet51/1     11.0.45.4/24         up         up              9214           
Loopback1        25.0.1.4/32          up         up             65535           
Loopback2        25.0.2.4/32          up         up             65535           
Management1      172.28.135.39/20     up         up              1500           
Vlan100          100.100.100.1/24     up         up              1500           
Vlan300          30.0.4.1/24          up         up              1500
```
## show lldp neighbors

```
Last table change time   : 1 day, 6:01:50 ago
Number of table inserts  : 14
Number of table deletes  : 10
Number of table drops    : 0
Number of table age-outs : 0

Port         Neighbor Device ID                          Neighbor Port ID   TTL 
---------- ------------------------------------------- -------------------- --- 
Et49/1       smv462.sjc.aristanetworks.com               Ethernet2/1        120 
Et50/1       cmp308.sjc.aristanetworks.com               Ethernet3/3/1      120 
Et51/1       ta368.sjc.aristanetworks.com                Ethernet49/1       120 
Ma1          r161-rack3-tor42.sjc.aristanetworks.com     Ethernet14         120
```
## show running-config

```
! Command: show running-config
! device: ta367 (DCS-7280SR2K-48C6-M, EOS-4.25.1F-20348152.oslorel (engineering build))
!
! boot system flash:/oslo-rel-20349931.swi
!
prompt %H.%D{%H:%M:%S}%P
terminal length 0
alias agents bash ls -lrt /var/log/agents/
alias c bash clear
alias cc clear counters
alias core bash ls -lrt /var/core/
alias cp clear platform fap counters
alias log bash sudo tail -f /var/log/messages
alias ls bash ls -lrt /var/log/agents
alias senz show interface counter error | nz
alias shmc show int | awk '/^[A-Z]/ { intf = $1 } /, address is/ { print intf, $6 }'
alias snz show interface counter | nz
alias spd show port-channel %1 detail all
alias sqnz show interface counter queue | nz
alias srnz show interface counter rate | nz
alias top show proc top
!
daemon TerminAttr
   exec /usr/bin/TerminAttr -ingestgrpcurl=172.28.136.21:9910 -cvcompression=gzip -ingestauth=key,eossuper -smashexcludes=ale,flexCounter,hardware,kni,pulse,strata -ingestexclude=/Sysdb/cell/1/agent,/Sysdb/cell/2/agent -ingestvrf=default -taillogs
   no shutdown
!
vlan internal order ascending range 4020 4090
!
load-interval default 5
!
transceiver qsfp default-mode 4x10G
!
service routing protocols model multi-agent
!
logging console debugging
logging monitor debugging
!
hostname ta367
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
aaa root secret sha512 $6$39jFJJLC92/tfRSR$FDX6NbWreQk8PEESV.6UWDR5qfpa6cSkvExAYHTxjSH7r3/Rrp/.U4Lm1MJMOf2ET2Xf52Fk23dpy6NWB9aZv1
aaa authentication policy local allow-nopassword-remote-login
!
username admin privilege 15 role network-admin nopassword
username arista secret sha512 $6$6xDUKLwsR6Ox26ZB$Eh.cd5p4SGnrNaoVAKQT5qIJFO2DCPEC9zglV3kR0TjkXH10Ll7aA9kqVGc4CtpU/6itGedC7F5KMzS07Z4qY/
username cvpadmin privilege 15 secret sha512 $6$VZQIOoRSDVGdF91/$3l4AQyO9kwEJJ4k.6JiG7AdFvQ7djVt70cGSjtB2jqroswgfsXkVtLrqQSAIeIJ/vpzbuyHbY3Pm1QC.0PXXk.
!
clock timezone US/Pacific
!
tunnel-ribs
   tunnel-rib system-tunnel-rib
      source-protocol static
      source-protocol isis segment-routing preference 65
      source-protocol bgp labeled-unicast
      source-protocol nexthop-group
      source-protocol rsvp-ler
      source-protocol ldp
!
vlan 100,300
!
vrf instance vrfa
!
vrf instance vrfb
!
interface Ethernet1
   switchport mode trunk
!
interface Ethernet2
!
interface Ethernet3
!
interface Ethernet4
!
interface Ethernet5
!
interface Ethernet6
!
interface Ethernet7
!
interface Ethernet8
!
interface Ethernet9
!
interface Ethernet10
!
interface Ethernet11
!
interface Ethernet12
!
interface Ethernet13
!
interface Ethernet14
!
interface Ethernet15
!
interface Ethernet16
!
interface Ethernet17
!
interface Ethernet18
!
interface Ethernet19
!
interface Ethernet20
!
interface Ethernet21
!
interface Ethernet22
!
interface Ethernet23
!
interface Ethernet24
!
interface Ethernet25
!
interface Ethernet26
!
interface Ethernet27
!
interface Ethernet28
!
interface Ethernet29
!
interface Ethernet30
!
interface Ethernet31
!
interface Ethernet32
!
interface Ethernet33
!
interface Ethernet34
!
interface Ethernet35
!
interface Ethernet36
!
interface Ethernet37
!
interface Ethernet38
!
interface Ethernet39
!
interface Ethernet40
!
interface Ethernet41
!
interface Ethernet42
!
interface Ethernet43
!
interface Ethernet44
!
interface Ethernet45
!
interface Ethernet46
!
interface Ethernet47
!
interface Ethernet48
!
interface Ethernet49/1
   description R1-E2/1
   mtu 9214
   no switchport
   ip address 11.0.14.4/24
   ipv6 enable
   ipv6 address ::11:0:14:4/124
   isis enable 0
   isis network point-to-point
   isis authentication mode md5 level-2
   isis authentication key 7 j4Dubk9Vcnjaq8//RS41uw== level-2
!
interface Ethernet50/1
   description R2-E3/3/1
   mtu 9214
   no switchport
   ip address 11.0.24.4/24
   ipv6 enable
   ipv6 address ::11:0:24:4/124
   isis enable 0
   isis network point-to-point
   isis authentication mode md5 level-2
   isis authentication key 7 j4Dubk9Vcnjaq8//RS41uw== level-2
!
interface Ethernet51/1
   description R5-E49/1
   mtu 9214
   no switchport
   ip address 11.0.45.4/24
   ipv6 enable
   ipv6 address ::11:0:45:4/124
   isis enable 0
   isis network point-to-point
   isis authentication mode md5 level-2
   isis authentication key 7 j4Dubk9Vcnjaq8//RS41uw== level-2
!
interface Ethernet52/1
!
interface Ethernet53/1
!
interface Ethernet54/1
!
interface Loopback1
   ip address 25.0.1.4/32
   ipv6 address ::25:0:1:4/128
   isis enable 0
   isis passive
!
interface Loopback2
   ip address 25.0.2.4/32
   ipv6 address ::25:0:2:4/128
   node-segment ipv4 index 44
   node-segment ipv6 index 46
   isis enable 0
   isis passive
!
interface Management1
   ip address 172.28.135.39/20
!
interface Vlan100
   vrf vrfa
   ip address 100.100.100.1/24
!
interface Vlan300
   ip address 30.0.4.1/24
!
ip access-list GNMI
   10 permit tcp any any eq gnmi
!
ip routing
ip routing vrf vrfa
ip routing vrf vrfb
!
ip prefix-list LDP-FECs
   seq 10 permit 25.0.2.1/32
   seq 20 permit 25.0.2.2/32
   seq 30 permit 25.0.2.3/32
   seq 40 permit 25.0.2.4/32
   seq 50 permit 25.0.2.5/32
   seq 60 permit 25.0.2.6/32
!
ipv6 unicast-routing
!
monitor session 1 source Ethernet50/1 tx
monitor session 1 source Ethernet51/1 tx
monitor session 1 destination Cpu
!
ip route 10.80.0.0/12 172.28.128.1
ip route 10.240.0.0/14 172.28.128.1
ip route 172.16.0.0/12 172.28.128.1
!
mpls ip
!
mpls ldp
   router-id 25.0.2.4
   transport-address interface Loopback2
   fec filter prefix-list LDP-FECs
   no shutdown
!
mpls icmp fragmentation-needed tunneling
mpls icmp ttl-exceeded tunneling
!
router bgp 64000
   router-id 25.0.1.4
   maximum-paths 4 ecmp 4
   neighbor MP_BGP peer group
   neighbor MP_BGP remote-as 64000
   neighbor MP_BGP update-source Loopback2
   neighbor MP_BGP send-community extended
   neighbor MP_BGP maximum-routes 0
   neighbor v4_iBGP_RR peer group
   neighbor v4_iBGP_RR remote-as 64000
   neighbor v4_iBGP_RR update-source Loopback1
   neighbor v4_iBGP_RR additional-paths receive
   neighbor v4_iBGP_RR maximum-routes 0
   neighbor v6_iBGP_RR peer group
   neighbor v6_iBGP_RR remote-as 64000
   neighbor v6_iBGP_RR update-source Loopback1
   neighbor v6_iBGP_RR maximum-routes 0
   neighbor 25.0.1.5 peer group v4_iBGP_RR
   neighbor 25.0.2.5 peer group MP_BGP
   neighbor ::25:0:1:5 peer group v6_iBGP_RR
   redistribute connected
   !
   address-family evpn
      neighbor default encapsulation mpls next-hop-self source-interface Loopback2
      neighbor MP_BGP activate
   !
   address-family ipv4
      no neighbor MP_BGP activate
      no neighbor v6_iBGP_RR activate
   !
   address-family ipv6
      neighbor v6_iBGP_RR activate
   !
   address-family vpn-ipv4
      neighbor MP_BGP activate
      neighbor default encapsulation mpls next-hop-self source-interface Loopback2
   !
   address-family vpn-ipv6
      neighbor MP_BGP activate
      no neighbor v4_iBGP_RR activate
      no neighbor v6_iBGP_RR activate
      neighbor default encapsulation mpls next-hop-self source-interface Loopback2
   !
   vrf vrfa
      rd 25.0.2.4:100
      route-target import evpn 100:100
      route-target export evpn 100:100
      redistribute connected
!
router isis 0
   net 49.0001.0250.0000.1004.00
   is-hostname R4
   router-id ipv4 25.0.1.4
   is-type level-2
   lsp purge origination-identification
   log-adjacency-changes
   timers local-convergence-delay protected-prefixes
   spf-interval 1 150 150
   timers lsp refresh 65000
   timers lsp min-remaining-lifetime 65535
   authentication mode md5 level-2
   graceful-restart
   graceful-restart t2 level-2 300
   graceful-restart restart-hold-time 300
   authentication key 7 j4Dubk9Vcnjaq8//RS41uw== level-2
   !
   address-family ipv4 unicast
      bfd all-interfaces
      fast-reroute ti-lfa mode node-protection
   !
   address-family ipv6 unicast
      bfd all-interfaces
      fast-reroute ti-lfa mode node-protection
   !
   segment-routing mpls
      no shutdown
      adjacency-segment allocation sr-peers backup-eligible
!
banner login
------------------------------------------------------------------------------------------

                     This device is in use for the Orange POC

  Please contact dpowders@arista.com before making any changes

-------------------------------------------------------------------------------------------
EOF
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
Arista DCS-7280SR2K-48C6-M-F
Hardware version: 20.01
Serial number: JAS18070010
Hardware MAC address: 7483.ef73.592b
System MAC address: 7483.ef73.592b

Software image version: 4.25.1F-20348152.oslorel (engineering build)
Architecture: i686
Internal build version: 4.25.1F-20348152.oslorel
Internal build ID: 21839e6b-0fd0-4fdc-86f1-919012c49df3

Uptime: 1 weeks, 1 days, 5 hours and 5 minutes
Total memory: 32813280 kB
Free memory: 29678716 kB
```
