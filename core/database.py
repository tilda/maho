from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from .models.base import Base

async def create_database():
    engine = create_async_engine('sqlite+aiosqlite:///maho.db')
    session = async_sessionmaker(engine, expire_on_commit=False)
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)