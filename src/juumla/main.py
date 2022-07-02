from requests import get, exceptions
from rich import print
from urllib3 import disable_warnings
from src.juumla.settings import props
from src.juumla.modules.version import get_version

disable_warnings()


def start(args) -> None:
    " Try to connect to the host and check status code condition "

    try:

        response: str = get(args.u, **props)
        status_code: int = response.status_code
        body: str = response.text

        status_error = f"[bold white on red]> Host returned status code: {status_code}"

        if response.ok:
            detect_joomla(args, body)
        else:
            return print(status_error)

    except exceptions as error:
        return print(f"[red]> Error when trying to connect to host: {args.u} | {error} [/]")


def detect_joomla(args, body) -> None:
    " Detect Joomla with body response "

    print("[yellow]> Checking if target is running Joomla... [/]")

    if '<meta name="generator" content="Joomla!' in body: get_version(args)
    else:
        return print("[red][-] Target is not running Joomla apparently [/]")