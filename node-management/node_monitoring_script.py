# node_monitoring_script.py
import os
import time
from scapy.all import *

# Set node IP addresses and names
nodes = {"node1": "192.168.1.100", "node2": "192.168.1.101", "node3": "192.168.1.102"}

# Function to check node status
def check_node_status(node_name, node_ip):
    response = os.system("ping -c 1 " + node_ip)
    if response == 0:
        print(f"{node_name} is online")
    else:
        print(f"{node_name} is offline")

# Monitor nodes
while True:
    for node_name, node_ip in nodes.items():
        check_node_status(node_name, node_ip)
    time.sleep(10)
