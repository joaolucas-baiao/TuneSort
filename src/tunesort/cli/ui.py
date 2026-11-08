from rich.console import Console
console = Console()

def limpar_tela():
    if console.is_terminal:
        print("\033[H\033[2J\033[3J", end="", flush=True)