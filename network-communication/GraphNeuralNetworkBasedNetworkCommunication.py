# Graph Neural Network-based Network Communication for PiNet-Manager
import numpy as np
from graph_neural_network import GraphNeuralNetwork

class GraphNeuralNetworkBasedNetworkCommunication:
    def __init__(self, network_topology):
        self.network_topology = network_topology
        self.gnn = GraphNeuralNetwork()

    def define_network(self):
        self.gnn.define_network(self.network_topology)

    def communicate(self):
        return self.gnn.communicate()

    def get_communication_result(self):
        return self.communicate()
