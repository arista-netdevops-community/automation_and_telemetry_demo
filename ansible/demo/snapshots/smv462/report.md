# smv462 Commands Output

## Table of Contents

- [show lldp neighbors](#show-lldp-neighbors)
- [show ip interface brief](#show-ip-interface-brief)
- [show interfaces description](#show-interfaces-description)
- [show version](#show-version)
- [show running-config](#show-running-config)
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
Et11/1.11                      up             up                 
Et11/1.12                      up             up                 
Et11/1.13                      up             up                 
Et11/1.14                      up             up                 
Et11/1.15                      up             up                 
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
Ma1                            up             up
```
## show ip interface brief

```
Address 
Interface          IP Address           Status    Protocol        MTU   Owner   
------------------ -------------------- --------- ----------- --------- ------- 
Ethernet1/1        11.0.12.1/24         up        up             9214           
Ethernet2/1        11.0.14.1/24         up        up             9214           
Ethernet3/1        11.0.15.1/24         up        up             9214           
Ethernet11/1       unassigned           up        up             1500           
Ethernet11/1.11    111.0.0.1/20         up        up             1500           
Ethernet11/1.12    112.0.0.1/30         up        up             1500           
Ethernet11/1.13    113.0.0.1/30         up        up             1500           
Ethernet11/1.14    114.0.0.1/30         up        up             1500           
Ethernet11/1.15    115.0.0.1/30         up        up             1500           
Loopback1          25.0.1.1/32          up        up            65535           
Loopback2          25.0.2.1/32          up        up            65535           
Management1        172.28.134.246/20    up        up             1500
```
## show lldp neighbors

```
Last table change time   : 2:21:47 ago
Number of table inserts  : 8
Number of table deletes  : 4
Number of table drops    : 0
Number of table age-outs : 0

Port        Neighbor Device ID                          Neighbor Port ID    TTL 
--------- ------------------------------------------- --------------------- --- 
Et1/1       cmp308.sjc.aristanetworks.com               Ethernet3/1/1       120 
Et2/1       ta367.sjc.aristanetworks.com                Ethernet49/1        120 
Et3/1       ta368.sjc.aristanetworks.com                Ethernet50/1        120 
Ma1         r161-rack3-tor42.sjc.aristanetworks.com     Ethernet17          120
```
## show running-config

```
! Command: show running-config
! device: smv462 (DCS-7280CR3K-32P4, EOS-4.25.1F)
!
! boot system flash:/EOS-4.25.1F.swi
!
prompt %H.%D{%H:%M:%S}%P
terminal length 0
terminal width 150
alias a show act
alias agents bash ls -lrt /var/log/agents/
alias b6 show ipv bgp sum
alias bc bash clear
alias bs sh ip bgp sum
alias bv show bgp vpn-ipv4
alias c config term
alias core bash ls -lrt /var/core/
alias hc show hardware capacity utilization percent exceed 50
alias hd sh ip bgp | egrep ">E"
alias hd6 sh ipv6 bgp | egrep ">E"
alias i show int status
alias ii show ip int brief
alias ln show lldp nei
alias log bash sudo tail -f /var/log/messages
alias m show run | more
alias senz show interface counter error | nz
alias shmc show int | awk '/^[A-Z]/ { intf = $1 } /, address is/ { print intf, $6 }'
alias snz show interface counter | nz
alias spd show port-channel %1 detail all
alias sqnz show interface counter queue | nz
alias sri show run interface
alias srnz show interface counter rate | nz
alias sro show run sec router ospf
alias top show proc top
!
daemon TerminAttr
   exec /usr/bin/TerminAttr -ingestgrpcurl=172.28.136.21:9910 -cvcompression=gzip -ingestauth=key,eossuper -smashexcludes=ale,flexCounter,hardware,kni,pulse,strata -ingestexclude=/Sysdb/cell/1/agent,/Sysdb/cell/2/agent -ingestvrf=default -taillogs
   no shutdown
!
vlan internal order ascending range 4020 4090
!
load-interval default 1
!
transceiver qsfp default-mode 4x10G
!
ip dhcp relay server 172.22.22.11
!
service routing protocols model multi-agent
!
logging format sequence-numbers
!
hostname smv462
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
username arista secret sha512 $6$/CQpDVBC3FQewrfh$e0PUsC6HmP2grdGk1QB8.5Hc2Bjh8EERieFwVezURlx/C9G0JYlsGZAtzIa4LPW6lS/oKtlmIvxEW1VFRijct1
username cvpadmin privilege 15 secret sha512 $6$VZQIOoRSDVGdF91/$3l4AQyO9kwEJJ4k.6JiG7AdFvQ7djVt70cGSjtB2jqroswgfsXkVtLrqQSAIeIJ/vpzbuyHbY3Pm1QC.0PXXk.
!
clock timezone PST8PDT
!
tunnel-ribs
   tunnel-rib system-tunnel-rib
      source-protocol static
      source-protocol isis segment-routing preference 50
      source-protocol bgp labeled-unicast
      source-protocol nexthop-group
      source-protocol rsvp-ler
      source-protocol ldp preference 55
!
vlan 11,100
!
vrf instance VPN1
!
vrf instance VPN2
!
interface Ethernet1/1
   description R2-E3/1/1
   mtu 9214
   no switchport
   ip address 11.0.12.1/24
   ipv6 enable
   ipv6 address ::11:0:12:1/124
   isis enable 0
   isis network point-to-point
   isis authentication mode md5 level-2
   isis authentication key 7 j4Dubk9Vcnjaq8//RS41uw== level-2
!
interface Ethernet2/1
   description R4-E49/1
   mtu 9214
   no switchport
   ip address 11.0.14.1/24
   ipv6 enable
   ipv6 address ::11:0:14:1/124
   isis enable 0
   isis network point-to-point
   isis authentication mode md5 level-2
   isis authentication key 7 j4Dubk9Vcnjaq8//RS41uw== level-2
!
interface Ethernet3/1
   description R5-E50/1
   mtu 9214
   no switchport
   ip address 11.0.15.1/24
   ipv6 enable
   ipv6 address ::11:0:15:1/124
   isis enable 0
   isis network point-to-point
   isis authentication mode md5 level-2
   isis authentication key 7 j4Dubk9Vcnjaq8//RS41uw== level-2
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
   speed forced 10000full
!
interface Ethernet10/1
   speed forced 100gfull
!
interface Ethernet10/3
   speed forced 10000full
!
interface Ethernet11/1
   speed forced 10000full
   no switchport
!
interface Ethernet11/1.11
   encapsulation dot1q vlan 11
   ip address 111.0.0.1/20
   ipv6 address ::111:0:0:1/118
!
interface Ethernet11/1.12
   encapsulation dot1q vlan 12
   ip address 112.0.0.1/30
   ipv6 address ::112:0:0:1/126
!
interface Ethernet11/1.13
   encapsulation dot1q vlan 13
   vrf VPN1
   ip address 113.0.0.1/30
   ipv6 address ::113:0:0:1/126
!
interface Ethernet11/1.14
   encapsulation dot1q vlan 14
   vrf VPN2
   ip address 114.0.0.1/30
   ipv6 address ::114:0:0:1/126
!
interface Ethernet11/1.15
   encapsulation dot1q vlan 15
   ip address 115.0.0.1/30
   ipv6 address ::115:0:0:1/126
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
interface Ethernet33/1
!
interface Ethernet34/1
!
interface Ethernet35/1
!
interface Ethernet36/1
!
interface Loopback1
   ip address 25.0.1.1/32
   ipv6 address ::25:0:1:1/128
   isis enable 0
   isis passive
!
interface Loopback2
   ip address 25.0.2.1/32
   ipv6 address ::25:0:2:1/128
   node-segment ipv4 index 14
   node-segment ipv6 index 16
   isis enable 0
   isis passive
!
interface Management1
   ip address 172.28.134.246/20
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
   router-id 25.0.1.1
   transport-address interface Loopback2
   fec filter prefix-list LDP-FECs
   no shutdown
!
router bgp 64000
   router-id 25.0.1.1
   maximum-paths 4 ecmp 4
   neighbor BGP_LU peer group
   neighbor BGP_LU remote-as 64015
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
   neighbor 25.0.2.3 remote-as 64000
   neighbor 25.0.2.3 update-source Loopback2
   neighbor 25.0.2.3 send-community extended
   neighbor 25.0.2.3 maximum-routes 12000
   neighbor 25.0.2.5 peer group MP_BGP
   neighbor 112.0.0.2 remote-as 64012
   neighbor 112.0.0.2 maximum-routes 0
   neighbor 115.0.0.2 peer group BGP_LU
   neighbor ::25:0:1:5 peer group v6_iBGP_RR
   neighbor ::112:0:0:2 remote-as 64012
   neighbor ::112:0:0:2 maximum-routes 0
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
      no neighbor BGP_LU activate
      no neighbor MP_BGP activate
      no neighbor v4_iBGP_RR activate
      no neighbor v6_iBGP_RR activate
      neighbor 25.0.2.3 activate 6pe
      neighbor ::112:0:0:2 activate
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
      rd 25.0.2.1:100
      route-target import vpn-ipv4 100:100
      route-target import vpn-ipv6 100:100
      route-target export vpn-ipv4 100:100
      route-target export vpn-ipv6 100:100
      neighbor 113.0.0.2 remote-as 64013
      neighbor 113.0.0.2 maximum-routes 0
      neighbor ::113:0:0:2 remote-as 64013
      neighbor ::113:0:0:2 maximum-routes 0
      redistribute connected
      !
      address-family ipv6
         neighbor ::113:0:0:2 activate
   !
   vrf VPN2
      rd 25.0.2.1:200
      route-target import vpn-ipv4 200:200
      route-target import vpn-ipv6 200:200
      route-target export vpn-ipv4 200:200
      route-target export vpn-ipv6 200:200
      neighbor 114.0.0.2 remote-as 64014
      neighbor 114.0.0.2 maximum-routes 0
      neighbor ::114:0:0:2 remote-as 64014
      neighbor ::114:0:0:2 maximum-routes 0
      redistribute connected
      !
      address-family ipv6
         neighbor ::114:0:0:2 activate
!
router isis 0
   net 49.0001.0250.0000.1001.00
   is-hostname R1
   router-id ipv4 25.0.1.1
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

------------------------------------------------------------------------------------------
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
Arista DCS-7280CR3K-32P4-F
Hardware version: 11.00
Serial number: JPE19362870
Hardware MAC address: fcbd.673c.0ec1
System MAC address: fcbd.673c.0ec1

Software image version: 4.25.1F
Architecture: i686
Internal build version: 4.25.1F-20001546.4251F
Internal build ID: 31358597-3f9d-49cf-b0a5-c16d16d21617

Uptime: 0 weeks, 3 days, 20 hours and 44 minutes
Total memory: 65859944 kB
Free memory: 62106264 kB
```
