# node_manager.py
import asyncio
from aiohttp import ClientSession
from cryptography.hazmat.primitives import serialization

class NodeManager:
    def __init__(self, node_list: list):
        self.node_list = node_list
        self.session = ClientSession()

    async def node_health_check(self):
        tasks = []
        for node in self.node_list:
            task = asyncio.create_task(self._check_node_health(node))
            tasks.append(task)
        results = await asyncio.gather(*tasks)
        return results

    async def _check_node_health(self, node: str):
        async with self.session.get(f"http://{node}:8080/health") as response:
            if response.status == 200:
                return {"node": node, "status": "healthy"}
            else:
                return {"node": node, "status": "unhealthy"}

    async def node_registration(self, node: str, public_key: str):
        async with self.session.post(f"http://{node}:8080/register", json={"public_key": public_key}) as response:
            if response.status == 201:
                return {"node": node, "status": "registered"}
            else:
                return {"node": node, "status": "registration failed"}

    async def node_deregistration(self, node: str):
        async with self.session.post(f"http://{node}:8080/deregister") as response:
            if response.status == 200:
                return {"node": node, "status": "deregistered"}
            else:
                return {"node": node, "status": "deregistration failed"}
