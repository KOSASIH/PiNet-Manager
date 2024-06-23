class PiNetManagerDevice:
    def __init__(self, data: dict):
        self.id = data["id"]
        self.name = data["name"]
        self.ip_address = data["ip_address"]

    def __repr__(self) -> str:
        return f"<PiNetManagerDevice: {self.name} ({self.ip_address})>"
