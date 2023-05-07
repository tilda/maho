from core.cog import Cog
from discord import app_commands
import discord
from ruamel.yaml import YAML

class PcrMapping(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    yaml = YAML() # please tell me there's a better way to do this
    config = yaml.load(open('config.yaml').read())
    
    
    @app_commands.command()
    @app_commands.guilds(config['pcr']['guild_id'])
    @app_commands.checks.has_any_role('Ameth', 'Nightmare')
    async def add_pcrmember(self, ctx: discord.Interaction, user: discord.Member):
        """Admin-only - adds the project member role to a user."""
        await user.add_roles(discord.Object(self.config['pcr']['member_role']), reason=f'Project member addition from {ctx.user!s}')
        return await ctx.response.send_message(f':white_check_mark: Added member role to {user!s}')
        
async def setup(bot):
    await bot.add_cog(PcrMapping(bot))