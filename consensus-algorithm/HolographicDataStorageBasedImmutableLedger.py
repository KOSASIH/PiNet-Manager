# Holographic Data Storage-based Immutable Ledger for PiNet-Manager
import numpy as np
from holographic_data_storage import HolographicDataStorage

class HolographicDataStorageBasedImmutableLedger:
    def __init__(self):
        self.hds = HolographicDataStorage()

    def add_block(self, block):
        self.hds.store(block)

    def get_block(self, block_hash):
        return self.hds.retrieve(block_hash)

    def get_latest_block(self):
        return self.hds.get_latest_block()
