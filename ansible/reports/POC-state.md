
# Validate State Report

**Table of Contents:**

- [Validate State Report](validate-state-report)
  - [Test Results Summary](#test-results-summary)
  - [Failed Test Results Summary](#failed-test-results-summary)
  - [All Test Results](#all-test-results)

## Test Results Summary

### Summary Totals

| Total Tests | Total Tests Passed | Total Tests Failed |
| ----------- | ------------------ | ------------------ |
| 70 | 64 | 6 |

### Summary Totals Devices Under Tests

| DUT | Total Tests | Tests Passed | Tests Failed | Categories Failed |
| --- | ----------- | ------------ | ------------ | ----------------- |
| DC1-SPINE1 |  15 | 14 | 1 | Reload Cause |
| DC1-SPINE2 |  15 | 14 | 1 | Reload Cause |
| DC1-LEAF1A |  11 | 10 | 1 | Reload Cause |
| DC1-LEAF1B |  11 | 10 | 1 | Reload Cause |
| DC1-LEAF2A |  9 | 8 | 1 | Reload Cause |
| DC1-LEAF2B |  9 | 8 | 1 | Reload Cause |

### Summary Totals Per Category

| Test Category | Total Tests | Tests Passed | Tests Failed |
| ------------- | ----------- | ------------ | ------------ |
| NTP |  6 | 6 | 0 |
| Interface State |  20 | 20 | 0 |
| LLDP Topology |  16 | 16 | 0 |
| IP Reachability |  16 | 16 | 0 |
| BGP |  6 | 6 | 0 |
| Reload Cause |  6 | 0 | 6 |

## Failed Test Results Summary

| Test ID | Node | Test Category | Test Description | Test | Test Result | Failure Reason |
| ------- | ---- | ------------- | ---------------- | ---- | ----------- | -------------- |
| 65 | DC1-SPINE1 | Reload Cause | Reload Cause: Reload requested by the user | Reload Cause | FAIL | Reload Cause: Unknown |
| 66 | DC1-SPINE2 | Reload Cause | Reload Cause: Reload requested by the user | Reload Cause | FAIL | Reload Cause: Unknown |
| 67 | DC1-LEAF1A | Reload Cause | Reload Cause: Reload requested by the user | Reload Cause | FAIL | Reload Cause: Unknown |
| 68 | DC1-LEAF1B | Reload Cause | Reload Cause: Reload requested by the user | Reload Cause | FAIL | Reload Cause: Unknown |
| 69 | DC1-LEAF2A | Reload Cause | Reload Cause: Reload requested by the user | Reload Cause | FAIL | Reload Cause: Unknown |
| 70 | DC1-LEAF2B | Reload Cause | Reload Cause: Reload requested by the user | Reload Cause | FAIL | Reload Cause: Unknown |

## All Test Results

| Test ID | Node | Test Category | Test Description | Test | Test Result | Failure Reason |
| ------- | ---- | ------------- | ---------------- | ---- | ----------- | -------------- |
| 1 | DC1-SPINE1 | NTP | Synchronised with NTP server | NTP | PASS |  |
| 2 | DC1-SPINE2 | NTP | Synchronised with NTP server | NTP | PASS |  |
| 3 | DC1-LEAF1A | NTP | Synchronised with NTP server | NTP | PASS |  |
| 4 | DC1-LEAF1B | NTP | Synchronised with NTP server | NTP | PASS |  |
| 5 | DC1-LEAF2A | NTP | Synchronised with NTP server | NTP | PASS |  |
| 6 | DC1-LEAF2B | NTP | Synchronised with NTP server | NTP | PASS |  |
| 7 | DC1-SPINE1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet1 | PASS |  |
| 8 | DC1-SPINE1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet2 | PASS |  |
| 9 | DC1-SPINE1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet4 | PASS |  |
| 10 | DC1-SPINE1 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet5 | PASS |  |
| 11 | DC1-SPINE2 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet1 | PASS |  |
| 12 | DC1-SPINE2 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet2 | PASS |  |
| 13 | DC1-SPINE2 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet4 | PASS |  |
| 14 | DC1-SPINE2 | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet5 | PASS |  |
| 15 | DC1-LEAF1A | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet1 | PASS |  |
| 16 | DC1-LEAF1A | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet2 | PASS |  |
| 17 | DC1-LEAF1A | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet3 | PASS |  |
| 18 | DC1-LEAF1A | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet4 | PASS |  |
| 19 | DC1-LEAF1B | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet1 | PASS |  |
| 20 | DC1-LEAF1B | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet2 | PASS |  |
| 21 | DC1-LEAF1B | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet3 | PASS |  |
| 22 | DC1-LEAF1B | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet4 | PASS |  |
| 23 | DC1-LEAF2A | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet1 | PASS |  |
| 24 | DC1-LEAF2A | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet2 | PASS |  |
| 25 | DC1-LEAF2B | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet1 | PASS |  |
| 26 | DC1-LEAF2B | Interface State | Ethernet Interface Status & Line Protocol == "up" | Ethernet2 | PASS |  |
| 27 | DC1-SPINE1 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet1 - remote: DC1-LEAF1A_Ethernet1 | PASS |  |
| 28 | DC1-SPINE1 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet2 - remote: DC1-LEAF1B_Ethernet1 | PASS |  |
| 29 | DC1-SPINE1 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet4 - remote: DC1-LEAF2A_Ethernet1 | PASS |  |
| 30 | DC1-SPINE1 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet5 - remote: DC1-LEAF2B_Ethernet1 | PASS |  |
| 31 | DC1-SPINE2 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet1 - remote: DC1-LEAF1A_Ethernet2 | PASS |  |
| 32 | DC1-SPINE2 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet2 - remote: DC1-LEAF1B_Ethernet2 | PASS |  |
| 33 | DC1-SPINE2 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet4 - remote: DC1-LEAF2A_Ethernet2 | PASS |  |
| 34 | DC1-SPINE2 | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet5 - remote: DC1-LEAF2B_Ethernet2 | PASS |  |
| 35 | DC1-LEAF1A | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet1 - remote: DC1-SPINE1_Ethernet1 | PASS |  |
| 36 | DC1-LEAF1A | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet2 - remote: DC1-SPINE2_Ethernet1 | PASS |  |
| 37 | DC1-LEAF1B | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet1 - remote: DC1-SPINE1_Ethernet2 | PASS |  |
| 38 | DC1-LEAF1B | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet2 - remote: DC1-SPINE2_Ethernet2 | PASS |  |
| 39 | DC1-LEAF2A | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet1 - remote: DC1-SPINE1_Ethernet4 | PASS |  |
| 40 | DC1-LEAF2A | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet2 - remote: DC1-SPINE2_Ethernet4 | PASS |  |
| 41 | DC1-LEAF2B | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet1 - remote: DC1-SPINE1_Ethernet5 | PASS |  |
| 42 | DC1-LEAF2B | LLDP Topology | lldp topology - validate peer and interface | local: Ethernet2 - remote: DC1-SPINE2_Ethernet5 | PASS |  |
| 43 | DC1-SPINE1 | IP Reachability | ip reachability test p2p links | Source: DC1-SPINE1_Ethernet1 - Destination: DC1-LEAF1A_Ethernet1 | PASS |  |
| 44 | DC1-SPINE1 | IP Reachability | ip reachability test p2p links | Source: DC1-SPINE1_Ethernet2 - Destination: DC1-LEAF1B_Ethernet1 | PASS |  |
| 45 | DC1-SPINE1 | IP Reachability | ip reachability test p2p links | Source: DC1-SPINE1_Ethernet4 - Destination: DC1-LEAF2A_Ethernet1 | PASS |  |
| 46 | DC1-SPINE1 | IP Reachability | ip reachability test p2p links | Source: DC1-SPINE1_Ethernet5 - Destination: DC1-LEAF2B_Ethernet1 | PASS |  |
| 47 | DC1-SPINE2 | IP Reachability | ip reachability test p2p links | Source: DC1-SPINE2_Ethernet1 - Destination: DC1-LEAF1A_Ethernet2 | PASS |  |
| 48 | DC1-SPINE2 | IP Reachability | ip reachability test p2p links | Source: DC1-SPINE2_Ethernet2 - Destination: DC1-LEAF1B_Ethernet2 | PASS |  |
| 49 | DC1-SPINE2 | IP Reachability | ip reachability test p2p links | Source: DC1-SPINE2_Ethernet4 - Destination: DC1-LEAF2A_Ethernet2 | PASS |  |
| 50 | DC1-SPINE2 | IP Reachability | ip reachability test p2p links | Source: DC1-SPINE2_Ethernet5 - Destination: DC1-LEAF2B_Ethernet2 | PASS |  |
| 51 | DC1-LEAF1A | IP Reachability | ip reachability test p2p links | Source: DC1-LEAF1A_Ethernet1 - Destination: DC1-SPINE1_Ethernet1 | PASS |  |
| 52 | DC1-LEAF1A | IP Reachability | ip reachability test p2p links | Source: DC1-LEAF1A_Ethernet2 - Destination: DC1-SPINE2_Ethernet1 | PASS |  |
| 53 | DC1-LEAF1B | IP Reachability | ip reachability test p2p links | Source: DC1-LEAF1B_Ethernet1 - Destination: DC1-SPINE1_Ethernet2 | PASS |  |
| 54 | DC1-LEAF1B | IP Reachability | ip reachability test p2p links | Source: DC1-LEAF1B_Ethernet2 - Destination: DC1-SPINE2_Ethernet2 | PASS |  |
| 55 | DC1-LEAF2A | IP Reachability | ip reachability test p2p links | Source: DC1-LEAF2A_Ethernet1 - Destination: DC1-SPINE1_Ethernet4 | PASS |  |
| 56 | DC1-LEAF2A | IP Reachability | ip reachability test p2p links | Source: DC1-LEAF2A_Ethernet2 - Destination: DC1-SPINE2_Ethernet4 | PASS |  |
| 57 | DC1-LEAF2B | IP Reachability | ip reachability test p2p links | Source: DC1-LEAF2B_Ethernet1 - Destination: DC1-SPINE1_Ethernet5 | PASS |  |
| 58 | DC1-LEAF2B | IP Reachability | ip reachability test p2p links | Source: DC1-LEAF2B_Ethernet2 - Destination: DC1-SPINE2_Ethernet5 | PASS |  |
| 59 | DC1-SPINE1 | BGP | ArBGP is configured and operating | ArBGP | PASS |  |
| 60 | DC1-SPINE2 | BGP | ArBGP is configured and operating | ArBGP | PASS |  |
| 61 | DC1-LEAF1A | BGP | ArBGP is configured and operating | ArBGP | PASS |  |
| 62 | DC1-LEAF1B | BGP | ArBGP is configured and operating | ArBGP | PASS |  |
| 63 | DC1-LEAF2A | BGP | ArBGP is configured and operating | ArBGP | PASS |  |
| 64 | DC1-LEAF2B | BGP | ArBGP is configured and operating | ArBGP | PASS |  |
| 65 | DC1-SPINE1 | Reload Cause | Reload Cause: Reload requested by the user | Reload Cause | FAIL | Reload Cause: Unknown |
| 66 | DC1-SPINE2 | Reload Cause | Reload Cause: Reload requested by the user | Reload Cause | FAIL | Reload Cause: Unknown |
| 67 | DC1-LEAF1A | Reload Cause | Reload Cause: Reload requested by the user | Reload Cause | FAIL | Reload Cause: Unknown |
| 68 | DC1-LEAF1B | Reload Cause | Reload Cause: Reload requested by the user | Reload Cause | FAIL | Reload Cause: Unknown |
| 69 | DC1-LEAF2A | Reload Cause | Reload Cause: Reload requested by the user | Reload Cause | FAIL | Reload Cause: Unknown |
| 70 | DC1-LEAF2B | Reload Cause | Reload Cause: Reload requested by the user | Reload Cause | FAIL | Reload Cause: Unknown |
