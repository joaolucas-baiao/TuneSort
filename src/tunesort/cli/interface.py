import questionary
from rich.console import Console

def mostrar_menu():
    try:
        escolha = questionary.select(
            "TuneSort • MUSIC LIBRARY ORGANIZER\n"
            "\nO que desejas fazer? :)",
            choices=[
                questionary.Choice(title="Analisar músicas curtidas", value="curtidas"),
                questionary.Choice(title="Organizar gêneros musicais", value="organizar"),
                questionary.Choice(title="Criar playlists automaticamente", value="playlist"),
                questionary.Choice(title="Configurações", value="config"),
                questionary.Choice(title="Sobre o TuneSort", value="sobre"),
                questionary.Choice(title="Sair", value="sair")
            ]).unsafe_ask()
        return escolha.upper()
    except KeyboardInterrupt:
        return "sair"