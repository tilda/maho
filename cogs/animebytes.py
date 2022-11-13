from discord.ext import commands
from discord import app_commands
import discord
from aiohttp import ClientSession
from typing import Literal
import Paginator
from textwrap import shorten
from html import unescape

class AnimeBytes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    @app_commands.describe(search_type='Category to search in. Anime contains most things')
    async def ablookup(self, ctx, lookup: str, search_type: Literal['anime', 'music']):
        def process_links(results):
            return ', '.join(f'[{title}]({link})' for title, link in results["Links"].items())


        # https://animebytes.tv/scrape.php?torrent_pass={:passkey}&username={:username}&type={:type[music|anime]}
        async with ClientSession() as http:
            async with http.get(
                    'https://animebytes.tv/scrape.php', params={
                        'torrent_pass': self.bot.config["services"]["animebytes"],
                        'username': self.bot.config["services"]["animebytes_username"],
                        'searchstr': lookup,
                        'type': search_type
                    }) as ab:
                try:
                    search = await ab.json()
                    matches = search['Matches']
                    results_amount = search['Results']
                    search_results = search['Groups']
                except:
                    return await ctx.response.send_message('Could not get results. Likely was not able to find what you were looking for.')

                results_embeds = []
                for results in search_results:
                    embed = discord.Embed(
                        title=unescape(results['FullName']),
                        description=f'{shorten(results["Description"], width=320, placeholder="...")}',
                        color=0x69d1c5
                    )
                    try:
                        links = process_links(results)
                    except: 
                        pass # we likely don't have links so fall back
                    else:
                        embed.add_field(name='Links', value=process_links(results))
                    embed.set_thumbnail(url=results["Image"])
                    embed.set_footer(text=f'Category: {results["CategoryName"]}, ID: {results["ID"]}')
                    results_embeds.append(embed)

                await Paginator.Simple().start(ctx, pages=results_embeds)


async def setup(bot):
    await bot.add_cog(AnimeBytes(bot))