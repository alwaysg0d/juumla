from rich.console import Console
console = Console()

def get_banner() -> str:
    " Return Juumla's banner "

    console.print("""[bold yellow]
jUuMlA - 0.1.6
most overrated joomla scanner
[/]""")