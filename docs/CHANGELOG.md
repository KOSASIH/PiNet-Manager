Changelog
=========

### v1.0.0

* Initial release
* Added device listing and filtering
* Added device details and configuration
* Added remote command execution
* Added real-time monitoring and logging

### v1.1.0

* Improved API performance
* Added support for multiple device types
* Fixed bug in device configuration update

### v1.2.0

* Added CLI tool for easy usage
* Improved error handling and logging
* Fixed bug in device creation

Code Files: 

api.py

```python
1. import requests
2. from flask import Flask, jsonify, request
3. 
4. app = Flask(__name__)
5. 
6. devices = []
7. 
8. @app.route('/devices', methods=['GET'])
9. def get_devices():
10.    return jsonify(devices)
11. 
12. @app.route('/devices/:id', methods=['GET'])
13. def get_device(id):
14.    device = next((d for d in devices if d['id'] == id), None)
15.    if device is None:
16.        return jsonify({'error': 'Device not found'}), 404
17.    return jsonify(device)
18. 
19. @app.route('/devices', methods=['POST'])
20. def create_device():
21.    data = request.get_json()
22.    device = {'id': len(devices) + 1, 'name': data['name'], 'ip_address': data['ip_address']}
23.    devices.append(device)
24.    return jsonify(device), 201
25. 
26. @app.route('/devices/:id', methods=['PATCH'])
27. def update_device(id):
28.    device = next((d for d in devices if d['id'] == id), None)
29.    if device is None:
30.        return jsonify({'error': 'Device not found'}), 404
31.    data = request.get_json()
32.    device['name'] = data['name']
33.    device['ip_address'] = data['ip_address']
34.    return jsonify(device)
35. 
36. @app.route('/devices/:id', methods=['DELETE'])
37. def delete_device(id):
38.    device = next((d for d in devices if d['id'] == id), None)
39.    if device is None:
40.        return jsonify({'error': 'Device not found'}), 404
41.    devices.remove(device)
42.    return jsonify({'message': 'Device deleted'})
43. 
44. if __name__ == '__main__':
45.    app.run(debug=True)
```

cli.py

```python
1. import argparse
2. import requests
3. 
4. def list_devices():
5.    response = requests.get('http://localhost:5000/devices')
6.    devices = response.json()
7.    for device in devices:
8.        print(f"  {device['id']}: {device['name']} ({device['ip_address']})")
9. 
10. def get_device(id):
11.    response = requests.get(f"http://localhost:5000/devices/{id}")
12.    device = response.json()
13.    print(f"Device {id}:")
14.    print(f"  Name: {device['name']}")
15.    print(f"  IP Address: {device['ip_address']}")
16. 
17. def update_device(id):
18.    data = {'name': input("Enter new name: "), 'ip_address': input("Enter new IP address: ")}
19.    response = requests.patch(f"http://localhost:5000/devices/{id}", json=data)
20.    print(f"Device {id} updated successfully")
21. 
22. def create_device():
23.    data = {'name': input("Enter name: "), 'ip_address': input("Enter IP address: ")}
24.    response = requests.post('http://localhost:5000/devices', json=data)
25.    device_id = response.json()['id']
26.    print(f"Device created successfully with ID {device_id}")
27. 
28. def delete_device(id):
29.    response = requests.delete(f"http://localhost:5000/devices/{id}")
30.    print(f"Device {id} deleted successfully")
31. 
32. def main():
33.    parser = argparse.ArgumentParser(description="PiNet-Manager CLI")
34.    parser.add_argument("command", help="Command to execute (list, get, update, create, delete)")
35.    args = parser.parse_args()
36. 
37.    if args.command == "list":
38.        list_devices()
39.    elif args.command == "get":
40.        id = int(input("Enter device ID: "))
41.        get_device(id)
42.    elif args.command == "update":
43.        id = int(input("Enter device ID: "))
44.        update_device(id)
45.    elif args.command == "create":
46.        create_device()
47.    elif args.command == "delete":
48.        id = int(input("Enter device ID: "))
49.        delete_device(id)
50.    else:
51.        print("Invalid command")
52. 
53. if __name__ == '__main__':
54.    main()
```

device.py

```python
1. class Device:
2.    def __init__(self, id, name, ip_address):
3.        self.id = id
4.        self.name = name
5.        self.ip_address = ip_address
6. 
7.    def __repr__(self):
8.        return f"<Device: {self.name} ({self.ip_address})>"
```

utils.py

```python
1. import ipaddress
2. 
3. def validate_ip_address(ip_address):
4.    try:
5.        ipaddress.IPv4Address(ip_address)
6.        return True
7.    except ValueError:
8.        return False
```

These docs/code files provide a comprehensive overview of the PiNet-Manager project, including its features, usage, and implementation details.
