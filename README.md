# ARP-with-Python
Detecting ARP spoofing attacks with python scapy library.
In the script above we are building our own ARP table using a dictionary and then
checking to see whether the packet we receive has changed an entry. 
NOTE: We’ll assume that any packet that changes the state of our table is malicious.
Scapy library provides us with the ability to manipulate packets.
Run the script above onthe terminal:

    kali> git clone https://github.com/ALLann123/ARP-with-Python.git
    kali> python3 arp_detector.py

To test if it works run the tool arpspoof on a target e.g metasploitable2 machine connected to the same network as the kali machine and after sometime cancel the arp attack using ctrl+c and observe the output by the script above detecting the attack.
![detectiom_arp](https://github.com/user-attachments/assets/ea960050-ef2d-4f13-90b1-a119575bb8ba)
![arp attack](https://github.com/user-attachments/assets/c01c8f47-04b8-4aaf-a4b4-ef13e113a7bb)



