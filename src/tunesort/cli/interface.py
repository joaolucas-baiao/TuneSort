import questionary
from rich.console import Console

def mostrar_menu():
    try:
        escolha = questionary.select(
            "TuneSort • MUSIC LIBRARY ORGANIZER\n"
            "\nO que desejas fazer? :)",
            choices=[
                "Analisar músicas curtidas",
                "Organizar gêneros musicais",
                "Criar playlists automaticamente",
                "Configurações",
                "Sobre o TuneSort",
                "Sair"
            ]).unsafe_ask()
        return escolha
    except KeyboardInterrupt:
        console = Console()
        console.print("! PROGRAMA INTERROMPIDO !", style="bold red")