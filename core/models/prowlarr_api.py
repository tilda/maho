from typing import Awaitable
from gracy import BaseEndpoint, Gracy, GracyConfig, LogEvent, LogLevel
from httpx import AsyncClient as HttpxAsyncClient

class ProwlarrAPIConfig:
    def __init__(self, instance_url: str):
        BASE_URL = instance_url
        SETTINGS = GracyConfig(
            log_request=LogEvent(LogLevel.DEBUG),
            log_response=LogEvent(LogLevel.INFO, "Requested {URL} in {ELAPSED}")
        )

class ProwlarrEndpoint(BaseEndpoint):
    HEALTH_CHECKS = "/health"
    
class ProwlarrAPIWrapper(Gracy[str]):
    def __init__(self, instance_url: str, api_key: str) -> None:
        self.instance_url = instance_url
        self.api_key = api_key
        self.Config = ProwlarrAPIConfig(instance_url)
        
        super().__init__()

    def _create_client(self) -> HttpxAsyncClient:
        client = super()._create_client()
        client.headers['X-Api-Key'] = self.api_key
        return client
    
    async def get_health_checks(self) -> Awaitable[dict]:
        return await self.get(ProwlarrEndpoint.HEALTH_CHECKS)