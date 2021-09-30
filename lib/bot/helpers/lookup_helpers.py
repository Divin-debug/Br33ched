from typing import List

from lib.core.utils import format_date, hide_password
from lib.weleakinfo.models import APIReponse


def format_breaches(response: APIReponse, show_query: bool, *flags) -> List[str]:
    breaches: List[str] = []

    for leak in response.results:
        if flags and '--detailed' in flags:
            date = format_date(leak.date)
            sources = ', '.join(leak.sources) or 'none'

            if show_query:
                breaches.append(
                    f'{leak.email}:{leak.password.ljust(20)} | Date: {date} | Sources: {sources}'
                )
            else:
                breaches.append(
                    f'{leak.password.ljust(20)} | Date: {date} | Sources: {sources}'
                )

        else:
            if show_query:
                breaches.append(f'{leak.email}:{leak.password}')
            else:
                breaches.append(leak.password)

    return breaches
