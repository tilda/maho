from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession, async_sessionmaker
from .models.base import Base

async def create_database():
    engine = create_async_engine('sqlite+aiosqlite:///maho.db')
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
    return engine

def create_db_session(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(engine, expire_on_commit=False)