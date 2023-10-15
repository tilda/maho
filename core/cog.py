from discord.ext import commands
from discord.app_commands import check
from discord import Interaction
from core.bot import MahoBot

class Cog(commands.Cog):
    def __init__(self, bot):
        self.bot: MahoBot = bot
        super().__init__(bot)
    
    @property
    def config(self):
        return self.bot.config
    
    @check
    @staticmethod
    def is_owner(ctx: Interaction):
        return ctx.client.is_owner(ctx.user.id)