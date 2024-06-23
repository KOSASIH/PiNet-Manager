# Quantum-Resistant Signature Scheme for PiNet-Manager
import hashlib
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend

class QuantumResistantSignature:
    def __init__(self, private_key):
        self.private_key = serialization.load_pem_private_key(
            private_key,
            password=None,
            backend=default_backend()
        )

    def sign(self, message):
        signer = ec.ECDSA(self.private_key, ec.ECDSA(hashes.SHA256()))
        signature = signer.sign(message)
        return signature

    def verify(self, message, signature):
        verifier = ec.ECDSA(self.private_key, ec.ECDSA(hashes.SHA256()))
        try:
            verifier.verify(message, signature)
            return True
        except InvalidSignature:
            return False
