# lib/visualization/network_topology.py
import networkx as nx
import matplotlib.pyplot as plt

class NetworkTopology:
    def __init__(self, devices):
        self.devices = devices
        self.G = nx.Graph()

    def build_topology(self):
        for device in self.devices:
            self.G.add_node(device['id'])
            for neighbor in device['neighbors']:
                self.G.add_edge(device['id'], neighbor)

    def visualize(self):
        pos = nx.spring_layout(self.G)
        nx.draw(self.G, pos, with_labels=True, node_color='skyblue', node_size=1500, edge_color='black', linewidths=1, font_size=12)
        plt.show()

# src/network_manager.py
from lib.visualization.network_topology import NetworkTopology

class NetworkManager:
    def __init__(self, devices):
        self.devices = devices
        self.topology = NetworkTopology(devices)

    def visualize_network(self):
        self.topology.build_topology()
        self.topology.visualize()
