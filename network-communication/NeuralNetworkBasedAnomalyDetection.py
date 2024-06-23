# Neural Network-based Anomaly Detection for PiNet-Manager
import numpy as np
from neural_network import NeuralNetwork

class NeuralNetworkBasedAnomalyDetection:
    def __init__(self, network_data):
        self.network_data = network_data
        self.nn = NeuralNetwork()

    def define_neural_network(self):
        self.nn.define_neural_network(self.network_data)

    def detect_anomaly(self):
        return self.nn.detect_anomaly()

    def get_anomaly_score(self):
        return self.detect_anomaly()
