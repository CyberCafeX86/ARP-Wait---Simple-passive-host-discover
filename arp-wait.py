#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from scapy.all import sniff, ARP

discovered_hosts = set()

def process_packet(packet):
    if ARP not in packet:
        return

    for ip in (packet[ARP].psrc, packet[ARP].pdst):
        if ip not in discovered_hosts:
            discovered_hosts.add(ip)
            print(ip)

def main():
    sniff(filter="arp", prn=process_packet, store=False)

if __name__ == "__main__":
    main()

