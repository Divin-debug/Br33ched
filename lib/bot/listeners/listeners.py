import discord
from discord.ext import commands
from discord.ext.commands.core import cooldown
from typing import Any
import os
from lib.core import logger


class Listeners(commands.Cog):
    def __init__(self, bot: commands.AutoShardedBot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_connect(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
        logger.success(f'Connected to {self.bot.user}')

        await self.bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name='9,052,791,410 passwords | .invite',
            )
        )
