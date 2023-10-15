from discord.ext import commands
from aiohttp import ClientSession
import discord
from logbook import Logger, StreamHandler, INFO
from logbook.compat import redirect_logging
from sys import stdout
from .models.prowlarr_api import ProwlarrAPIWrapper
from transmission_rpc import Client as TransmissionClient

class MahoBot(commands.Bot):
    def __init__(self, config, *args, **kwargs):
        super().__init__(*args, **kwargs)
        redirect_logging()
        StreamHandler(stdout, level=INFO).push_application()
        self.log = Logger('maho')
        self.http_session = ClientSession()
        self.config = config
        self.home_base = discord.Object(id=self.config['bot']['home_base_id'])
        self.prowlarr_client = ProwlarrAPIWrapper(self.config['prowlarr']['host'], self.config['prowlarr']['api_key'])
        self.transmission_client = TransmissionClient(
            host=self.config['transmission']['host'],
            port=self.config['transmission']['port'],
            username=self.config['transmission']['username'],
            password=self.config['transmission']['password']
        )