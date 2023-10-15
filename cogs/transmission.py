from core.cog import Cog
import discord
from discord import app_commands

class Transmission(Cog):
    def __init__(self, bot):
        # aaa
        pass
    
    @app_commands.command()
    @app_commands.describe(torrent="A .torrent file to upload to Transmission")
    async def queue_torrent(self, ctx: discord.Interaction, torrent: discord.Asset):
        return