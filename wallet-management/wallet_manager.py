# wallet_manager.py
import hashlib
from ecdsa import SigningKey, VerifyingKey

class WalletManager:
    def __init__(self):
        self.wallets = {}

    def create_wallet(self, private_key: str):
        signing_key = SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
        verifying_key = signing_key.verifying_key
        public_key = verifying_key.to_string()
        wallet_id = hashlib.sha256(public_key).hexdigest()
        self.wallets[wallet_id] = {"private_key": private_key, "public_key": public_key}
        return wallet_id

    def get_wallet(self, wallet_id: str):
        return self.wallets.get(wallet_id)

    def sign_transaction(self, wallet_id: str, transaction: str):
        private_key = self.wallets[wallet_id]["private_key"]
        signing_key = SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
        signature = signing_key.sign(transaction.encode())
        return signature.hex()

async def main():
    wallet_manager = WalletManager()
    wallet_id = wallet_manager.create_wallet("private_key_here")
    print(wallet_id)
    wallet = wallet_manager.get_wallet(wallet_id)
    print(wallet)
    signature = wallet_manager.sign_transaction(wallet_id, "transaction_data_here")
    print(signature)

asyncio.run(main())
