# Distributed Ledger for PiNet-Manager
import hashlib
from collections import OrderedDict

class DistributedLedger:
    def __init__(self):
        self.ledger = OrderedDict()

    def add_block(self, block):
        block_hash = hashlib.sha256(str(block).encode()).hexdigest()
        self.ledger[block_hash] = block

    def get_block(self, block_hash):
        return self.ledger.get(block_hash)

    def get_latest_block(self):
        return list(self.ledger.values())[-1]
