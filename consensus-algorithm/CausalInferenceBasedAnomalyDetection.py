# Causal Inference-based Anomaly Detection for PiNet-Manager
import numpy as np
from causal_inference import CausalInference

class CausalInferenceBasedAnomalyDetection:
    def __init__(self, network_data):
        self.network_data = network_data
        self.ci = CausalInference()

    def define_causal_graph(self):
        self.ci.define_causal_graph(self.network_data)

    def detect_anomaly(self):
        return self.ci.detect_anomaly()

    get_anomaly_score(self):
        return self.ci.get_anomaly_score()
