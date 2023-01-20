from discord.ext import commands
import discord
from core.bot import MahoBot
from ruamel.yaml import YAML
from sys import stdout
import os
import asyncio


yaml = YAML()
config = yaml.load(open('config.yaml').read())
intents = discord.Intents.default()
intents.message_content = True
bot = MahoBot(
    config=config,
    intents=intents,
    command_prefix=config['bot']['prefix']
)

async def setup_bot():
    async with bot:
        for ext in os.listdir('cogs'):
            if ext.endswith('.py'):
                try:
                    bot.log.info(f'attempting to load {ext}')
                    ext = ext.replace('.py', '')
                    await bot.load_extension(f'cogs.{ext}')
                except Exception:
                    bot.log.error(f'failed to load {ext}', exc_info=True)
                else:
                    bot.log.info(f'successfully loaded {ext}')
        bot.log.info('also loading jishaku')
        await bot.load_extension('jishaku')
        await bot.start(config['bot']['token'])


if __name__ == "__main__":
    asyncio.run(setup_bot())