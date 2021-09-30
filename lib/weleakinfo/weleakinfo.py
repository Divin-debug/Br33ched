from lib.weleakinfo.models import APIReponse, Leak

import json
import asyncio
from typing import List
from discord.ext import commands
from lib.core import logger


async def lookup_query(
    bot: commands.AutoShardedBot, query: str, _type: str = 'email'
) -> APIReponse:
    async with bot.session.get(
        f'https://api.weleakinfo.to/api?value={query}&type={_type}&key={bot.api_key}'
    ) as response:
        if response.status == 429:
            await asyncio.sleep(1)
            return await lookup_query(query)

        content = json.loads(await response.text())

        if not content['success']:
            return APIReponse(success=False)

        breaches: List[Leak] = []
        for result in content['result']:
            if not ':' in result['line']:
                continue

            breaches.append(
                Leak(
                    email=result['line'].split(':')[0],
                    password=result['line'].split(':')[1],
                    date=result['last_breach'],
                    sources=result['sources'],
                ),
            )

        return APIReponse(success=True, results=breaches)
