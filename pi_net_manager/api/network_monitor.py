import scapy.all as scapy

def get_network_interfaces():
    return scapy.get_if_list()

def get_network_traffic(interface):
    packets = scapy.sniff(iface=interface, count=100)
    return packets

def get_device_arp_table(interface):
    arp_table = scapy.arping(interface, timeout=1)
    return arp_table

def get_device_dns_table(interface):
    dns_table = scapy.dns_query(interface, "google.com")
    return dns_table
