from discord.ext import commands
import discord

class AnimeBytes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.HybridCommand
    async def lookup(self, ctx, lookup: str):
        # https://animebytes.tv/scrape.php?torrent_pass={:passkey}&username={:username}&type={:type[music|anime]}
        