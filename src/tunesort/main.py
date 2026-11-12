from questionary import press_any_key_to_continue
from rich.panel import Panel
from rich.text import Text

from tunesort import __version__
from tunesort.cli import banner, interface, ui


def acao_curtidas():
    print("Em construção...")
def acao_organizar():
    print("Em construção...")
def acao_playlist():
    print("Em construção...")
def acao_config():
    print("Em construção...")
def sobre():
    conteudo = Text(justify="left")
    conteudo.append("[+] Descrição", style="bold white")
    conteudo.append("  •  ", style="bold dim")
    conteudo.append("Ferramenta CLI para organizar músicas e automatizar playlists do Spotify", style="bold cyan")

    conteudo.append("\n[+] Versão", style="bold white")
    conteudo.append("  •  ", style="bold dim")
    conteudo.append(f"v{__version__}", style="bold cyan")

    conteudo.append("\n[+] Autor", style="bold white")
    conteudo.append("  •  ", style="bold dim")
    conteudo.append("Jotlz - (João Lucas)", style="bold cyan")

    conteudo.append("\n[+] Projeto", style="bold white")
    conteudo.append("  •  ", style="bold dim")
    conteudo.append("https://github.com/joaolucas-baiao/TuneSort", style="bold dim cyan")

    ui.console.print(
            Panel(
                conteudo,
                title="[bold white]• SOBRE O TUNESORT • ",
                border_style="bold cyan",
                padding=(1, 1),
                expand=False
            )
    )

def main():
    acoes = {
            "curtidas" : acao_curtidas,
            "organizar" : acao_organizar,
            "playlist" : acao_playlist,
            "config" : acao_config,
            "sobre" : sobre
        }
    while True:
        ui.limpar_tela()
        banner.mostrar_banner()
        escolha = interface.mostrar_menu()
        if escolha == "sair":
            ui.console.print("! PROGRAMA ENCERRADO !", style="bold red")
            break
        acoes[escolha]()
        try:
            press_any_key_to_continue(message="Aperte qualquer tecla para continuar...").unsafe_ask()
        except KeyboardInterrupt:
            pass #* retorna ao menu

if __name__ == "__main__":
    main()