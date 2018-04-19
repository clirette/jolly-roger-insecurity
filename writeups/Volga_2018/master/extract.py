# mtoups - for VolgaCTF 2018
# read a pcap file, extract some stuff...
from scapy.all import *
import time

# rdpcap comes from scapy and loads in our pcap file
packets = rdpcap('capture.pcap')
# Let's iterate through every packet
for packet in packets:
    # We're only interested in TCP with source port 3306
    if packet.haslayer(TCP) and packet.sport == 3306:
            try:
                print(str(packet.load[254:].split('\x1a')[0]) + " " + str(packet.load[254:].split('\x1a')[1][:26]))
            except: continue # some packets aren't long enough, skip those
