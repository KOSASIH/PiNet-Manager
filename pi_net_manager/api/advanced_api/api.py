import requests
from pinet_manager.config import PiNetManagerConfig

class PiNetManagerAPI:
    def __init__(self, config: PiNetManagerConfig):
        self.config = config
        self.session = requests.Session()

    def get_device_list(self) -> list:
        response = self.session.get(f"{self.config.api_url}/devices")
        response.raise_for_status()
        return response.json()

    def get_device_details(self, device_id: int) -> dict:
        response = self.session.get(f"{self.config.api_url}/devices/{device_id}")
        response.raise_for_status()
        return response.json()

    def update_device(self, device_id: int, data: dict) -> None:
        response = self.session.patch(f"{self.config.api_url}/devices/{device_id}", json=data)
        response.raise_for_status()

    def create_device(self, data: dict) -> int:
        response = self.session.post(f"{self.config.api_url}/devices", json=data)
        response.raise_for_status()
        return response.json()["id"]

    def delete_device(self, device_id: int) -> None:
        response = self.session.delete(f"{self.config.api_url}/devices/{device_id}")
        response.raise_for_status()
