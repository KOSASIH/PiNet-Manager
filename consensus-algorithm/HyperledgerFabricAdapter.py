# Hyperledger Fabric Adapter for PiNet-Manager
import hashlib
from hyperledger.fabric.sdk import Client

class HyperledgerFabricAdapter:
    def __init__(self, channel_name, chaincode_name, peer_url):
        self.client = Client()
        self.channel_name = channel_name
        self.chaincode_name = chaincode_name
        self.peer_url = peer_url

    def invoke_chaincode(self, func, args):
        proposal_response = self.client.propose(
            channel_name=self.channel_name,
            chaincode_name=self.chaincode_name,
            fcn=func,
            args=args,
            peers=[self.peer_url]
        )
        if proposal_response.is_valid():
            return proposal_response.response.payload
        else:
            raise Exception("Invalid proposal response")

    def query_chaincode(self, func, args):
        query_response = self.client.query(
            channel_name=self.channel_name,
            chaincode_name=self.chaincode_name,
            fcn=func,
            args=args,
            peers=[self.peer_url]
        )
        if query_response.is_valid():
            return query_response.response.payload
        else:
            raise Exception("Invalid query response")
