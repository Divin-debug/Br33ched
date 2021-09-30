from colorama import Fore


def info(message: str) -> None:
    print(f'{Fore.BLUE}[{Fore.RESET}+{Fore.BLUE}]{Fore.RESET} {message}')


def warning(message: str) -> None:
    print(f'{Fore.YELLOW}[{Fore.RESET}!{Fore.YELLOW}]{Fore.RESET} {message}')


def error(message: str) -> None:
    print(f'{Fore.RED}[{Fore.RESET}!{Fore.RED}]{Fore.RESET} {message}')


def success(message: str) -> None:
    print(f'{Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} {message}')
