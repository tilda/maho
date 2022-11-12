from discord.ext import commands
from aiohttp import ClientSession
import discord
from transmission_rpc import Client as TransmissionClient

class HiyorinBot(commands.Bot):
    def __init__(self, config, logger, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log = logger
        self.http_session = ClientSession()
        self.bot_config = config
        self.transmission_client = TransmissionClient(
            host=self.bot_config['transmission']['host'],
            port=self.bot_config['transmission']['port'],
            username=self.bot_config['transmission']['username'],
            password=self.bot_config['transmission']['password']
        )