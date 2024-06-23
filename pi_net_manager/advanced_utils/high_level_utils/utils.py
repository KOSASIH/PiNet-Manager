import ipaddress

def validate_ip_address(ip_address: str) -> bool:
    try:
        ipaddress.IPv4Address(ip_address)
        return True
    except ValueError:
        return False
