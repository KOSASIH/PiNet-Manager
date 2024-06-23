# Homomorphic Encryption-based Voting for PiNet-Manager
import numpy as np
from phe import paillier

class HomomorphicEncryptionBasedVoting:
    def __init__(self, public_key, private_key):
        self.public_key = public_key
        self.private_key = private_key

    def encrypt_vote(self, vote):
        return paillier.encrypt(vote, self.public_key)

    def aggregate_votes(self, encrypted_votes):
        aggregated_vote = encrypted_votes[0]
        for vote in encrypted_votes[1:]:
            aggregated_vote += vote
        return aggregated_vote

    def decrypt_result(self, aggregated_vote):
        return paillier.decrypt(aggregated_vote, self.private_key)
