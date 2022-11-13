from discord.ext import commands
from aiohttp import ClientSession
import discord
from transmission_rpc import Client as TransmissionClient
from logbook import Logger, StreamHandler, INFO
from logbook.compat import redirect_logging
from sys import stdout
class HiyorinBot(commands.Bot):
    def __init__(self, config, *args, **kwargs):
        super().__init__(*args, **kwargs)
        redirect_logging()
        StreamHandler(stdout, level=INFO).push_application()
        self.log = Logger('hiyorin')
        self.http_session = ClientSession()
        self.config = config
        self.home_base = discord.Object(id=self.config['bot']['home_base_id'])
        self.transmission_client = TransmissionClient(
            host=self.config['transmission']['host'],
            port=self.config['transmission']['port'],
            username=self.config['transmission']['username'],
            password=self.config['transmission']['password']
        )
    
    async def setup_hook(self):
        # Copy global commands to home base and sync, so new commands
        # are added immediately
        self.tree.copy_global_to(guild=self.home_base)
        await self.tree.sync(guild=self.home_base)