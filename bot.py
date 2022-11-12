from discord.ext import commands
import discord
from core.bot import HiyorinBot
from ruamel.yaml import YAML
from logbook import Logger, StreamHandler, INFO
from logbook.compat import redirect_logging

redirect_logging()
StreamHandler(stdout, level=INFO).push_application
log = Logger("hiyorin")

yaml = YAML()
config = yaml.load(open('config.yaml').read())
bot = HiyorinBot(
    config=config,
    logger=log,
    intents=discord.Intents.default(),
    command_prefix='hiyorin '
)

bot.run(config['bot']['token'])
