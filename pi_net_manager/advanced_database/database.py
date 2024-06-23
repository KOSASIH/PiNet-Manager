# database.py
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

engine = create_async_engine("postgresql+asyncpg://user:password@host:port/dbname")
async_session = AsyncSession(engine)

class Database:
    async def get_devices_list(self) -> List[dict]:
        # Implement database query to retrieve devices list
        async with async_session() as session:
            result = await session.execute("SELECT * FROM devices")
            devices = [dict(row) for row in result]
            return devices
