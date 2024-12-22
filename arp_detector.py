from scapy.all import sniff, ARP, Ether

print("[+]Started ARP Detection")
print("-------------------------------------")

# Dictionary to store MAC-IP mapping
IP_MAC_Map = {}

def processPacket(packet):
    # Check if the packet has ARP and Ethernet layers
    if ARP in packet and Ether in packet:
        src_IP = packet[ARP].psrc
        src_MAC = packet[Ether].src

        # Check if the MAC address already exists in the map
        if src_MAC in IP_MAC_Map:
            if IP_MAC_Map[src_MAC] != src_IP:
                # Potential ARP spoofing detected
                old_IP = IP_MAC_Map[src_MAC]
                message = (
                    f"\n Possible ARP attack detected! \n"
                    f"The machine with MAC address {src_MAC} is pretending to be "
                    f"IP address {src_IP}. Previously it was associated with {old_IP}.\n"
                )
                print(message)
        else:
            # Update the MAC-IP mapping
            IP_MAC_Map[src_MAC] = src_IP

# Start sniffing ARP packets
sniff(filter="arp", store=0, prn=processPacket)
