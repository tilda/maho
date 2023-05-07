from discord.ext import commands

class Cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__(bot)
    
    @property
    def config(self):
        return self.bot.config