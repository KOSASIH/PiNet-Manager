# Blockchain-based Secure Communication for PiNet-Manager
import numpy as np
from blockchain import Blockchain

class BlockchainBasedSecureCommunication:
    def __init__(self):
        self.blockchain = Blockchain()

    def send_message(self, message):
        self.blockchain.add_block(message)

    def receive_message(self, block_hash):
        return self.blockchain.get_block(block_hash)

    def verify_message(self, message):
        return self.blockchain.verify_block(message)
