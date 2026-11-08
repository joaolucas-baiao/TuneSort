from tunesort import __version__
from tunesort.cli import ui
from rich.text import Text
from rich.panel import Panel
from rich.align import Align
from rich.console import Group

def mostrar_banner():
    banner = Text(justify="center")
    banner.append("    ████████╗██╗   ██╗███╗   ██╗███████╗███████╗ ██████╗ ██████╗ ████████╗  \n", style="bold #0B8185")
    banner.append("    ╚══██╔══╝██║   ██║████╗  ██║██╔════╝██╔════╝██╔═══██╗██╔══██╗╚══██╔══╝  \n", style="bold #0B8185")
    banner.append("   ██║   ██║   ██║██╔██╗ ██║█████╗  ███████╗██║   ██║██████╔╝   ██║     \n", style="bold #0B8185")
    banner.append("   ██║   ██║   ██║██║╚██╗██║██╔══╝  ╚════██║██║   ██║██╔══██╗   ██║     \n", style="bold #0B8185")
    banner.append("   ██║   ╚██████╔╝██║ ╚████║███████╗███████║╚██████╔╝██║  ██║   ██║     \n", style="bold #1F5F61")
    banner.append("   ╚═╝    ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝     \n", style="bold #1F5F61")

    subtitulo = Text(justify="left")
    subtitulo.append("• Descrição", style="bold white")
    subtitulo.append("  -  ", style="bold dim")
    subtitulo.append("Ferramenta CLI para organizar músicas e automatizar playlists do Spotify.", style="bold #092b5a")

    ascii_art = Group(banner, subtitulo)
    ui.console.print(
        Panel(
            Align.center(ascii_art),
            title="[bold white]TuneSort" + f"[bold green] v{__version__}",
            title_align="left",
            subtitle="[bold white]Made with" + "[bold #f05d67] ❤" + "[bold white] by" + "[bold #36544F] Jotlz",
            border_style="cyan",
            padding=(2, 2),
            width=110,
        )
    )