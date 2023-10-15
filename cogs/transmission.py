from typing import Optional
from core.cog import Cog
import discord
from discord import app_commands
import asyncio

class Transmission(Cog):
    def __init__(self, bot):
        # aaa
        pass
    
    @app_commands.command()
    @app_commands.check(Cog.is_owner)
    @app_commands.describe(torrent_file="A .torrent file to upload to Transmission")
    async def queue_torrent(self, ctx: discord.Interaction, torrent_file: discord.Attachment, label: Optional[str]):
        progress: discord.Message = await ctx.response.send_message('Got it, sending to Transmission.')
        
        try:
            async with asyncio.timeout(10):
                await self.bot.loop.run_in_executor(
                    None,
                    self.bot.transmission_client.add_torrent,
                    torrent=torrent_file.url,
                    labels=label
                )
        except TimeoutError:
            return await progress.edit(content='Request timed out. Did something catch on fire?')
        else:
            return await progress.edit(content=f'Successfully added {torrent_file.filename} to Transmission.')

async def setup(bot):
    await bot.add_cog(Transmission(bot))