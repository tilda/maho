from discord.ext import commands
import discord

class Prowlarr(commands.Cog):
    def __init__(self, bot):
        self.bot = bot