from discord.ext import commands
import discord
from core.bot import HiyorinBot
from ruamel.yaml import YAML

yaml = YAML()
config = yaml.load(open('config.yaml').read())
bot = HiyorinBot(
    config=config,
    intents=discord.Intents.default(),
    command_prefix='hiyorin '
)

bot.run(config['bot']['token'])
