# Blockchain-based Immutable Ledger for PiNet-Manager
import hashlib
from blockchain import Blockchain

class BlockchainBasedImmutableLedger:
    def __init__(self):
        self.blockchain = Blockchain()

    def add_block(self, block):
        block_hash = hashlib.sha256(str(block).encode()).hexdigest()
        self.blockchain.add_block(block, block_hash)

    def get_block(self, block_hash):
        return self.blockchain.get_block(block_hash)

    def get_latest_block(self):
        return self.blockchain.get_latest_block()
