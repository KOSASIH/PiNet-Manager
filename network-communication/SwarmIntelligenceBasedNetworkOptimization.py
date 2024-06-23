# Swarm Intelligence-based Network Optimization for PiNet-Manager
import numpy as np
from swarm_intelligence import SwarmIntelligence

class SwarmIntelligenceBasedNetworkOptimization:
    def __init__(self, network_topology):
        self.network_topology = network_topology
        self.si = SwarmIntelligence()

    def define_network(self):
        self.si.define_network(self.network_topology)

    def optimize_network(self):
        return self.si.optimize_network()

    def get_optimal_solution(self):
        return self.optimize_network()
