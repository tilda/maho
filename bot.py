from discord.ext import commands
import discord
from core.bot import HiyorinBot
from ruamel.yaml import YAML
from logbook import Logger, StreamHandler, INFO
from logbook.compat import redirect_logging
from sys import stdout
import os

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

if __name__ == "__main__":
    for ext in os.listdir("cogs"):
        if ext.endswith(".py"):
            try:
                log.info(f"attempting to load {ext}")
                ext = ext.replace(".py", "")
                bot.load_extension(f"ext.{ext}")
            except Exception:
                log.error(f"failed to load {ext}", exc_info=True)
            else:
                log.info(f"successfully loaded {ext}")
    log.info("loading jishaku")
    bot.load_extension("jishaku")

bot.run(config['bot']['token'])
