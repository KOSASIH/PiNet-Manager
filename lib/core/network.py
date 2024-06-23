import socket

class Network:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host, port):
        self.socket.connect((host, port))

    def send(self, data):
        self.socket.send(data.encode())

    def receive(self, buffer_size):
        return self.socket.recv(buffer_size).decode()

    def close(self):
        self.socket.close()
