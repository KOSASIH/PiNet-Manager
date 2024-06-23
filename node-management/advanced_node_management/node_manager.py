# node_manager.py
import asyncio
from aiohttp import ClientSession
from cryptography.hazmat.primitives import serialization

class NodeManager:
    def __init__(self, node_list: list):
        self.node_list = node_list
        self.session = ClientSession()

    async def get_node_info(self, node_id: str):
        async with self.session.get(f"http://{node_id}:8080/info") as response:
            return await response.json()

    async def update_node_config(self, node_id: str, config: dict):
        async with self.session.patch(f"http://{node_id}:8080/config", json=config) as response:
            return await response.json()

    async def start_node(self, node_id: str):
        async with self.session.post(f"http://{node_id}:8080/start") as response:
            return await response.json()

    async def stop_node(self, node_id: str):
        async with self.session.post(f"http://{node_id}:8080/stop") as response:
            return await response.json()

    async def get_node_list(self):
        nodes = []
        for node in self.node_list:
            info = await self.get_node_info(node)
            nodes.append({"id": node, "info": info})
        return nodes

async def main():
    node_manager = NodeManager(["node1", "node2", "node3"])
    nodes = await node_manager.get_node_list()
    print(nodes)

asyncio.run(main())
