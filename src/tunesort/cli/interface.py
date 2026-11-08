import questionary
def mostrar_menu():
    try:
        escolha = questionary.select(
            "TuneSort • Music Library Organizer\n"
            "\nO que desejas fazer? :)",
            choices=[
                questionary.Choice(title="Analisar músicas curtidas", value="curtidas"),
                questionary.Choice(title="Organizar gêneros musicais", value="organizar"),
                questionary.Choice(title="Criar playlists automaticamente", value="playlist"),
                questionary.Choice(title="Configurações", value="config"),
                questionary.Choice(title="Sobre o TuneSort", value="sobre"),
                questionary.Choice(title="Sair", value="sair")
            ],
            instruction="(Use as teclas direcionais)"
        ).unsafe_ask()
        return escolha
    except KeyboardInterrupt:
        return "sair"