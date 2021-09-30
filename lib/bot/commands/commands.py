from io import StringIO
from typing import Optional

import discord
from discord.ext import commands
from lib.bot.helpers.lookup_helpers import format_breaches
from lib.core import logger
from lib.weleakinfo.weleakinfo import lookup_query


class Commands(commands.Cog):
    def __init__(self, bot: commands.AutoShardedBot) -> None:
        self.bot = bot

    @commands.command(
        name='invite',
        brief='Invite the bot to your server',
        usage='.invite',
    )
    async def invite(self, ctx: commands.Context) -> None:
        await ctx.send(
            f'> Invite: {self.bot.bot_invite}\n'
            f'> Discord server: {self.bot.discord_invite}'
        )

    @commands.command(
        name='help',
        brief='Get help with commands',
        usage='.help ?<command>',
    )
    async def help(self, ctx: commands.Context, command: Optional[str] = None) -> None:
        if not command:
            message = '> Comands for **BR33CHED**\n\n'
            for _command in self.bot.commands:
                try:
                    if not _command.hidden:
                        message += (
                            f'> .{_command.name} ({_command.brief}) `{_command.usage}`\n'
                        )
                except Exception as e:
                    logger.error(f'Error adding message: {e}')

            return await ctx.send(message)

        try:
            _command = self.bot.get_command(command.lower())
        except Exception:
            return await self.help(ctx)
        else:
            if not _command:
                return await self.help(ctx)
            await ctx.send(f'> .{_command.name} ({_command.brief}) `{_command.usage}`')

    @commands.command(
        name='lookup',
        brief='Search data breaches for query',
        usage='.lookup <email | username | txt file> --detailed',
    )
    async def lookup(
        self, ctx: commands.Context, query: Optional[str], *, flags: Optional[str] = None
    ) -> None:
        # if (
        #     ctx.guild
        #     and ctx.guild.id == 871868316308889640
        #     and ctx.channel.id != 871889196523081798
        # ):
        #     return await ctx.send(
        #         '> Please use <#871889196523081798> or use the bot in its dms, you can also invite the bot to your own server using `.invite`.'
        #     )

        if not query:
            return await ctx.send('> Missing query.')

        logger.info(f'{ctx.author} ({ctx.author.id}) looked up {query}')

        async with ctx.typing():
            try:
                response = self.bot.cache[query]
            except KeyError:
                response = await lookup_query(self.bot, query)
                self.bot.cache[query] = response
            if not response.success and not response.results:
                return await ctx.send(f'> No data breaches for **{query}** found.')

            breaches = format_breaches(response, False, flags)

            try:
                return await ctx.send(
                    f'> Found **{len(breaches):,}** data breaches for **{query}**\n```\n%s\n```'
                    % '\n'.join(breaches)
                )
            except Exception:
                io = StringIO('\n'.join(breaches))
                return await ctx.send(
                    f'> Found **{len(breaches):,}** data breaches for **{query}**',
                    file=discord.File(io, 'breaches.txt'),
                )
