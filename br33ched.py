from typing import List

import aiohttp
import discord
import yaml
from discord.ext import commands, tasks

from lib.bot.commands import Commands
from lib.bot.listeners import Listeners
from lib.core import logger


class Br33ched(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(
            command_prefix='.',
            help_command=None,
            allowed_mentions=discord.AllowedMentions(
                everyone=False,
                users=False,
                roles=False,
                replied_user=True,
            ),
            intents=discord.Intents(
                guilds=True,
                members=True,
                messages=True,
                guild_messages=True,
            ),
            owner_ids=[497351998178328576],
        )

        with open('config.yml', encoding='utf-8') as f:
            config = yaml.safe_load(f)['br33ched']

        self.discord_invite = config['discord_invite']
        self.bot_invite = config['bot_invite']
        self.api_key = config['weleakinfo_api_key']

        self.token = config['token']

        self.session = aiohttp.ClientSession()

        self.cache = {}
        self.clear_cache.start()

        self.add_cog(Listeners(self))
        self.add_cog(Commands(self))

    @tasks.loop(hours=1)
    async def clear_cache(self) -> None:
        logger.info('Cleared cache')
        self.cache = {}


if __name__ == '__main__':
    br33ched = Br33ched()
    br33ched.run(br33ched.token)
