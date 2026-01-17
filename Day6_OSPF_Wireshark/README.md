# Day 6: OSPF Packet Analysis with Wireshark

**Objective:** Understand the OSPF neighbor discovery process by capturing and analyzing "Hello" packets using Wireshark.

## 🦈 Lab Scenario
* **Topology:** R1 and SW1 connected via a Layer 3 link (`10.1.1.0/30`).
* **Protocol:** OSPF Area 0.
* **Goal:** Capture the initial handshake and verify the parameters required for adjacency.

## ⚙️ Configuration Snippets

### R1 (Router)
```bash
interface GigabitEthernet0/0
 ip address 10.1.1.1 255.255.255.252
!
router ospf 1
 router-id 1.1.1.1
 network 10.1.1.0 0.0.0.3 area 0
SW1 (Layer 3 Switch)
Bash
ip routing
!
interface GigabitEthernet0/0
 no switchport
 ip address 10.1.1.2 255.255.255.252
!
router ospf 1
 router-id 2.2.2.2
 network 10.1.1.0 0.0.0.3 area 0
🔬 Wireshark Analysis (Packet Walk)
OSPF uses Hello Packets (Type 1) to find neighbors. For neighbors to form an adjacency, specific fields in this packet must match.

Key Fields Identified:
Destination IP: 224.0.0.5 (All OSPF Routers Multicast).

Area ID: 0.0.0.0 (Backbone Area).

Hello Interval: 10 seconds (Heartbeat).

Dead Interval: 40 seconds (If no Hello is received by then, the neighbor is considered dead).

Router Priority: 1 (Default for DR/BDR election).

(Screenshot showing the expanded OSPF Header details)

🧪 Verification
The adjacency was successfully formed after parameters matched:

 %OSPF-5-ADJCHG: Process 1, Nbr 1.1.1.1 on GigabitEthernet0/0 from LOADING to FULL, Loading Done