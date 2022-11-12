from discord.ext import commands
import discord
from core.bot import HiyorinBot
from ruamel.yaml import YAML
from logbook import Logger, StreamHandler, INFO
from logbook.compat import redirect_logging
from sys import stdout

redirect_logging()
StreamHandler(stdout, level=INFO).push_application
log = Logger("hiyorin")

yaml = YAML()
config = yaml.load(open('config.yaml').read())
intents = discord.Intents.default()
intents.message_content = True
bot = HiyorinBot(
    config=config,
    logger=log,
    intents=intents,
    command_prefix='hiyorin '
)

bot.run(config['bot']['token'])
