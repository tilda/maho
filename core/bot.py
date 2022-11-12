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