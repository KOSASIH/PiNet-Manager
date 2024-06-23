import logging
from pi_net_manager.utils.logging import setup_logging
from pi_net_manager.core.device_monitoring import DeviceMonitoring
from pi_net_manager.core.network_config import NetworkConfig

setup_logging()

class PiNetManager:
    def __init__(self):
        self.device_monitoring = DeviceMonitoring()
        self.network_config = NetworkConfig()

    def get_devices(self):
        return self.device_monitoring.get_devices()

    def get_device(self, device_id):
        return self.device_monitoring.get_device(device_id)
