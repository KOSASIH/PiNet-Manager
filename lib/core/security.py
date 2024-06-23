import hashlib

class Security:
    def __init__(self):
        self.hash_algorithm = hashlib.sha256

    def hash_password(self, password):
        return self.hash_algorithm(password.encode()).hexdigest()

    def verify_password(self, password, hashed_password):
        return self.hash_password(password) == hashed_password
