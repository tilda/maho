from discord.ext import commands
from discord import app_commands
import discord
from aiohttp import ClientSession
from typing import Literal
import Paginator

class AnimeBytes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    @app_commands.describe(search_type='Category to search in. Anime contains most things')
    async def ablookup(self, ctx, lookup: str, search_type: Literal['anime', 'music']):
        def process_links(links):
            links_list = ''
            for title, link in links.items():
                links_list += f'[{title}]({link})'
            return links_list


        # https://animebytes.tv/scrape.php?torrent_pass={:passkey}&username={:username}&type={:type[music|anime]}
        async with ClientSession() as http:
            async with http.get(
                    f'https://animebytes.tv/scrape.php', params={
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
                            title=results['FullName'],
                            description=f'*{results["Description"]}*',
                            color=0x69d1c5)
                        
                    self.bot.log.info(len(results["Description"]))
                    embed.add_field(name='Links', value=process_links(results))
                    embed.set_footer(text=f'Category: {results["CategoryName"]}, ID: {results["ID"]}')
                    results_embeds.append(embed)

                await Paginator.Simple().start(ctx, pages=results_embeds)


async def setup(bot):
    await bot.add_cog(AnimeBytes(bot))