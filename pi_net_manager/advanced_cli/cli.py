import argparse
from pinet_manager.api import PiNetManagerAPI
from pinet_manager.config import PiNetManagerConfig

class PiNetManagerCLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="PiNet-Manager CLI")
        self.parser.add_argument("-c", "--config", help="Path to configuration file")
        self.parser.add_argument("command", help="Command to execute (list, get, update, create, delete)")

    def parse_args(self) -> argparse.Namespace:
        return self.parser.parse_args()

    def run(self, args: argparse.Namespace) -> None:
        config = PiNetManagerConfig()
        config.load_config(args.config)

        api = PiNetManagerAPI(config)

        if args.command == "list":
            devices = api.get_device_list()
            print("Devices:")
            for device in devices:
                print(f"  {device['id']}: {device['name']} ({device['ip_address']})")
        elif args.command == "get":
            device_id = int(input("Enter device ID: "))
            device = api.get_device_details(device_id)
            print(f"Device {device_id}:")
            print(f"  Name: {device['name']}")
            print(f"  IP Address: {device['ip_address']}")
        elif args.command == "update":
            device_id = int(input("Enter device ID: "))
            data = {"name": input("Enter new name: "), "ip_address": input("Enter new IP address: ")}
            api.update_device(device_id, data)
            print(f"Device {device_id} updated successfully")
        elif args.command == "create":
            data = {"name": input("Enter name: "), "ip_address": input("Enter IP address: ")}
            device_id = api.create_device(data)
            print(f"Device created successfully with ID {device_id}")
        elif args.command == "delete":
            device_id = int(input("Enter device ID: "))
            api.delete_device(device_id)
            print(f"Device {device_id} deleted successfully")
        else:
            print("Invalid command")
