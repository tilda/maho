from ruamel.yaml import YAML
from discord.ext import commands
from aiohttp import ClientSession
import discord
from transmission_rpc import Client as TransmissionClient

class HiyorinBot(commands.Bot):
    def __init__(self, logger, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log = logger
        self.http_session = ClientSession()
        self.bot_config = YAML().load(open('config.yaml'))
        self.transmission_client = TransmissionClient