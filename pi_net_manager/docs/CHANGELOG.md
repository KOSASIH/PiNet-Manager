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

