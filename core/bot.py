from discord.ext import commands
from aiohttp import ClientSession
import discord
from transmission_rpc import Client as TransmissionClient

class HiyorinBot(commands.Bot):
    def __init__(self, config, logger, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log = logger
        self.http_session = ClientSession()
        self.config = config
        self.transmission_client = TransmissionClient(
            host=self.config['transmission']['host'],
            port=self.config['transmission']['port'],
            username=self.config['transmission']['username'],
            password=self.config['transmission']['password']
        )
    
    async def setup_hook(self):
        # Copy global commands to home base and sync, so new commands
        # are added immediately
        self.tree.copy_global_to(guild=self.config['bot']['home_base_id'])
        await self.tree.sync(self.config['bot']['home_base_id'])