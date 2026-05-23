from scapy.all import *

def process_packet(packet):
    if packet.haslayer(IP):
        print("\n=== Packet Captured ===")
        print(f"Source IP      : {packet[IP].src}")
        print(f"Destination IP : {packet[IP].dst}")
        print(f"Protocol       : {packet[IP].proto}")

print("Starting Network Sniffer...")
print("Press CTRL + C to stop.\n")

sniff(iface="Wi-Fi", prn=process_packet, store=False)