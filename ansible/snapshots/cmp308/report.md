# cmp308 Commands Output

## Table of Contents

- [show lldp neighbors](#show-lldp-neighbors)
- [show ip interface brief](#show-ip-interface-brief)
- [show interfaces description](#show-interfaces-description)
- [show version](#show-version)
- [show running-config](#show-running-config)
## show interfaces description

```
Interface                      Status         Protocol           Description
Et3/1/1                        up             up                 R1-E1/1
Et3/2/1                        up             up                 R3-E49/1
Et3/3/1                        up             up                 R4-E50/1
Et3/4/1                        up             up                 R5-E51/1
Et3/5/1                        up             up                 R6-E50/1
Et3/6/1                        down           notpresent         
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
Interface           IP Address           Status    Protocol       MTU   Owner   
------------------- -------------------- --------- ----------- -------- ------- 
Ethernet3/1/1       11.0.12.2/24         up        up            9214           
Ethernet3/2/1       11.0.23.2/24         up        up            9214           
Ethernet3/3/1       11.0.24.2/24         up        up            9214           
Ethernet3/4/1       11.0.25.2/24         up        up            9214           
Ethernet3/5/1       11.0.26.2/24         up        up            9214           
Ethernet3/10/1      unassigned           up        up            1500           
Ethernet3/10/1.11   121.0.0.1/20         up        up            1500           
Ethernet3/10/1.12   122.0.0.1/30         up        up            1500           
Ethernet3/10/1.13   123.0.0.1/30         up        up            1500           
Ethernet3/10/1.14   124.0.0.1/30         up        up            1500           
Ethernet3/10/1.15   125.0.0.1/30         up        up            1500           
Loopback1           25.0.1.2/32          up        up           65535           
Loopback2           25.0.2.2/32          up        up           65535           
Management1/1       172.28.135.145/20    up        up            1500           
Management1/2       unassigned           down      down          1500
```
## show lldp neighbors

```
Last table change time   : 1 day, 16:07:05 ago
Number of table inserts  : 21
Number of table deletes  : 15
Number of table drops    : 0
Number of table age-outs : 0

Port         Neighbor Device ID                          Neighbor Port ID   TTL 
---------- ------------------------------------------- -------------------- --- 
Et3/1/1      smv462.sjc.aristanetworks.com               Ethernet1/1        120 
Et3/2/1      ta366.sjc.aristanetworks.com                Ethernet49/1       120 
Et3/3/1      ta367.sjc.aristanetworks.com                Ethernet50/1       120 
Et3/4/1      ta368.sjc.aristanetworks.com                Ethernet51/1       120 
Et3/5/1      ta373.sjc.aristanetworks.com                Ethernet50/1       120 
Ma1/1        r161-rack3-tor42.sjc.aristanetworks.com     Ethernet10         120
```
## show running-config

```
! Command: show running-config
! device: cmp308 (DCS-7804-CH, EOS-4.25.1F-20348152.oslorel (engineering build))
!
! boot system flash:/oslo-rel-20349931.swi
!
prompt %H.%D{%H:%M:%S}%R%P
terminal length 0
alias agents bash ls -lrt /var/log/agents/
alias c bash clear
alias core bash ls -lrt /var/core/
alias log bash sudo tail -f /var/log/messages
alias senz show interface counter error | nz
alias shmc show int | awk '/^[A-Z]/ { intf = \$1 } /, address is/ { print intf, \$
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
transceiver qsfp default-mode 4x10G
!
ip dhcp relay server 172.22.22.11
!
service routing protocols model multi-agent
!
logging format sequence-numbers
!
hostname cmp308
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
username arista secret sha512 $6$2FDsZXmUn7qa4AA4$2vOmpZUe8bo7lRtGDz5ywDvgEulUnUKKBpNrT1Fq0cuXCB2CRJJlkLuC7f22BbbVzXphVBMYft81IGMdfi/5g1
username cvpadmin privilege 15 secret sha512 $6$VZQIOoRSDVGdF91/$3l4AQyO9kwEJJ4k.6JiG7AdFvQ7djVt70cGSjtB2jqroswgfsXkVtLrqQSAIeIJ/vpzbuyHbY3Pm1QC.0PXXk.
!
clock timezone PST8PDT
!
vrf instance VPN1
!
vrf instance VPN2
!
interface Ethernet3/1/1
   description R1-E1/1
   mtu 9214
   no switchport
   ip address 11.0.12.2/24
   ipv6 enable
   ipv6 address ::11:0:12:2/124
   isis enable 0
   isis network point-to-point
   isis authentication mode md5 level-2
   isis authentication key 7 j4Dubk9Vcnjaq8//RS41uw== level-2
!
interface Ethernet3/2/1
   description R3-E49/1
   mtu 9214
   no switchport
   ip address 11.0.23.2/24
   ipv6 enable
   ipv6 address ::11:0:23:2/124
   isis enable 0
   isis network point-to-point
   isis authentication mode md5 level-2
   isis authentication key 7 j4Dubk9Vcnjaq8//RS41uw== level-2
!
interface Ethernet3/3/1
   description R4-E50/1
   mtu 9214
   no switchport
   ip address 11.0.24.2/24
   ipv6 enable
   ipv6 address ::11:0:24:2/124
   isis enable 0
   isis network point-to-point
   isis authentication mode md5 level-2
   isis authentication key 7 j4Dubk9Vcnjaq8//RS41uw== level-2
!
interface Ethernet3/4/1
   description R5-E51/1
   mtu 9214
   no switchport
   ip address 11.0.25.2/24
   ipv6 enable
   ipv6 address ::11:0:25:2/124
   isis enable 0
   isis network point-to-point
   isis authentication mode md5 level-2
   isis authentication key 7 j4Dubk9Vcnjaq8//RS41uw== level-2
!
interface Ethernet3/5/1
   description R6-E50/1
   mtu 9214
   no switchport
   ip address 11.0.26.2/24
   ipv6 enable
   ipv6 address ::11:0:26:2/124
   isis enable 0
   isis network point-to-point
   isis authentication mode md5 level-2
   isis authentication key 7 j4Dubk9Vcnjaq8//RS41uw== level-2
!
interface Ethernet3/6/1
!
interface Ethernet3/7/1
!
interface Ethernet3/8/1
!
interface Ethernet3/10/1
   speed forced 10000full
   no switchport
!
interface Ethernet3/10/1.11
   encapsulation dot1q vlan 11
   ip address 121.0.0.1/20
   ipv6 address ::121:0:0:1/118
!
interface Ethernet3/10/1.12
   encapsulation dot1q vlan 12
   ip address 122.0.0.1/30
   ipv6 address ::122:0:0:1/126
!
interface Ethernet3/10/1.13
   encapsulation dot1q vlan 13
   vrf VPN1
   ip address 123.0.0.1/30
   ipv6 address ::123:0:0:1/126
!
interface Ethernet3/10/1.14
   encapsulation dot1q vlan 14
   vrf VPN2
   ip address 124.0.0.1/30
   ipv6 address ::124:0:0:1/126
!
interface Ethernet3/10/1.15
   encapsulation dot1q vlan 15
   ip address 125.0.0.1/30
   ipv6 address ::125:0:0:1/126
!
interface Ethernet3/10/2
   speed forced 10000full
!
interface Ethernet3/11/1
!
interface Ethernet3/12/1
!
interface Ethernet3/13/1
!
interface Ethernet3/14/1
!
interface Ethernet3/15/1
!
interface Ethernet3/16/1
!
interface Ethernet3/17/1
!
interface Ethernet3/18/1
!
interface Ethernet3/19/1
!
interface Ethernet3/20/1
!
interface Ethernet3/21/1
!
interface Ethernet3/22/1
!
interface Ethernet3/23/1
!
interface Ethernet3/24/1
!
interface Ethernet3/25/1
!
interface Ethernet3/26/1
!
interface Ethernet3/27/1
!
interface Ethernet3/28/1
!
interface Ethernet3/29/1
!
interface Ethernet3/30/1
!
interface Ethernet3/31/1
!
interface Ethernet3/32/1
!
interface Ethernet3/33/1
!
interface Ethernet3/34/1
!
interface Ethernet3/35/1
!
interface Ethernet3/36/1
!
interface Ethernet3/37/1
!
interface Ethernet3/38/1
!
interface Ethernet3/39/1
!
interface Ethernet3/40/1
!
interface Ethernet3/41/1
!
interface Ethernet3/42/1
!
interface Ethernet3/43/1
!
interface Ethernet3/44/1
!
interface Ethernet3/45/1
!
interface Ethernet3/46/1
!
interface Ethernet3/47/1
!
interface Ethernet3/48/1
!
interface Loopback1
   ip address 25.0.1.2/32
   ipv6 address ::25:0:1:2/128
   isis enable 0
   isis passive
!
interface Loopback2
   ip address 25.0.2.2/32
   ipv6 address ::25:0:2:2/128
   node-segment ipv4 index 24
   node-segment ipv6 index 26
   isis enable 0
   isis passive
!
interface Management1/1
   ip address 172.28.135.145/20
!
interface Management1/2
!
ip access-list GNMI
   10 permit tcp any any eq gnmi
!
ip routing
ip routing vrf VPN1
ip routing vrf VPN2
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
ipv6 unicast-routing vrf VPN1
ipv6 unicast-routing vrf VPN2
!
ip route 10.80.0.0/12 172.28.128.1
ip route 10.240.0.0/14 172.28.128.1
ip route 172.16.0.0/12 172.28.128.1
!
mpls ip
!
mpls ldp
   router-id 25.0.2.2
   transport-address interface Loopback2
   fec filter prefix-list LDP-FECs
   no shutdown
!
mpls icmp fragmentation-needed tunneling
mpls icmp ttl-exceeded tunneling
!
router bgp 64000
   router-id 25.0.1.2
   neighbor BGP_LU peer group
   neighbor BGP_LU remote-as 64025
   neighbor BGP_LU next-hop-self
   neighbor BGP_LU update-source Loopback2
   neighbor BGP_LU ebgp-multihop
   neighbor BGP_LU send-community extended
   neighbor BGP_LU maximum-routes 0
   neighbor MP_BGP peer group
   neighbor MP_BGP remote-as 64000
   neighbor MP_BGP next-hop-self
   neighbor MP_BGP update-source Loopback2
   neighbor MP_BGP send-community extended
   neighbor MP_BGP maximum-routes 0
   neighbor v4_iBGP_RR peer group
   neighbor v4_iBGP_RR remote-as 64000
   neighbor v4_iBGP_RR update-source Loopback1
   neighbor v4_iBGP_RR maximum-routes 0
   neighbor v6_iBGP_RR peer group
   neighbor v6_iBGP_RR remote-as 64000
   neighbor v6_iBGP_RR update-source Loopback1
   neighbor v6_iBGP_RR maximum-routes 0
   neighbor 25.0.1.5 peer group v4_iBGP_RR
   neighbor 25.0.2.5 peer group MP_BGP
   neighbor 122.0.0.2 remote-as 64022
   neighbor 122.0.0.2 maximum-routes 0
   neighbor 125.0.0.2 peer group BGP_LU
   neighbor ::25:0:1:5 peer group v6_iBGP_RR
   neighbor ::122:0:0:2 remote-as 64022
   neighbor ::122:0:0:2 maximum-routes 0
   redistribute connected
   !
   address-family evpn
      neighbor default encapsulation mpls next-hop-self source-interface Loopback2
      neighbor MP_BGP activate
   !
   address-family ipv4
      no neighbor BGP_LU activate
      no neighbor MP_BGP activate
      no neighbor v6_iBGP_RR activate
   !
   address-family ipv4 labeled-unicast
      neighbor BGP_LU activate
      neighbor MP_BGP activate
   !
   address-family ipv6
      no neighbor MP_BGP activate
      no neighbor v4_iBGP_RR activate
      no neighbor v6_iBGP_RR activate
      neighbor 25.0.2.1 activate 6pe
      neighbor ::122:0:0:2 activate
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
   vrf VPN1
      rd 25.0.2.2:100
      route-target import vpn-ipv4 100:100
      route-target import vpn-ipv6 100:100
      route-target export vpn-ipv4 100:100
      route-target export vpn-ipv6 100:100
      neighbor 123.0.0.2 remote-as 64023
      neighbor 123.0.0.2 maximum-routes 0
      neighbor ::123:0:0:2 remote-as 64023
      neighbor ::123:0:0:2 maximum-routes 0
      redistribute connected
      !
      address-family ipv6
         neighbor ::123:0:0:2 activate
   !
   vrf VPN2
      rd 25.0.2.2:200
      route-target import vpn-ipv4 200:200
      route-target import vpn-ipv6 200:200
      route-target export vpn-ipv4 200:200
      route-target export vpn-ipv6 200:200
      neighbor 124.0.0.2 remote-as 64024
      neighbor 124.0.0.2 maximum-routes 0
      neighbor ::124:0:0:2 remote-as 64024
      neighbor ::124:0:0:2 maximum-routes 0
      redistribute connected
      !
      address-family ipv6
         neighbor ::124:0:0:2 activate
!
router isis 0
   net 49.0001.0250.0000.1002.00
   is-hostname R2
   router-id ipv4 25.0.1.2
   is-type level-2
   lsp purge origination-identification
   log-adjacency-changes
   redistribute connected
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
Arista DCS-7804-CH
Hardware version: 11.02
Serial number: TMO20410350
Hardware MAC address: 985d.82ff.fea8
System MAC address: 985d.82ff.fea8

Software image version: 4.25.1F-20348152.oslorel (engineering build)
Architecture: i686
Internal build version: 4.25.1F-20348152.oslorel
Internal build ID: 21839e6b-0fd0-4fdc-86f1-919012c49df3

Uptime: 1 weeks, 3 days, 9 hours and 25 minutes
Total memory: 65859832 kB
Free memory: 60509524 kB
```
