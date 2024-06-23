class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class NetworkDevice:
    def __init__(self, ip_address, mac_address, device_name):
        self.ip_address = ip_address
        self.mac_address = mac_address
        self.device_name = device_name
