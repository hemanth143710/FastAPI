import aioredis
create_redis=aioredis.create_redis

from .settings import get_broker_settings


async def connect_redis() -> aioredis.Redis:
    broker_settings = get_broker_settings()
    return await create_redis(f"redis://{broker_settings.host}:{broker_settings.port}/{broker_settings.db}")
