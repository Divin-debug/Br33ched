def hide_password(password: str) -> str:
    return password[:3] + '*' * len(password[3:])


def format_date(date: str) -> str:
    if not date:
        return 'none   '

    if '-' in date:
        return date

    return date + '   '
