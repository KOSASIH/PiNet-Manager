# device_monitor.py
import asyncio
import websockets

async def monitor_devices():
    async with websockets.connect('ws://example.com/ws') as ws:
        while True:
            message = await ws.recv()
            # Process device data
            print(f'Received device data: {message}')

async def main():
    await monitor_devices()

asyncio.run(main())
