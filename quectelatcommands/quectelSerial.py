from scapy.all import *

# Load the provided packet capture file
pcap_file = "/home/pierr0t/begin.pcapng"

packets = PcapReader(pcap_file)


packets_summary = []

try:

    for packet in packets:
        packets_summary.append(packet.summary())
except:
    pass


for index in range(0, len(packets_summary)):
    if index > 39 and index < 64:
        print(packets_summary[index])

    if index > 3110 and index < 3168:
        print(packets_summary[index])

    if index > 8589 and index < 8671:
        print(packets_summary[index])
