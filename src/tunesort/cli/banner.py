from rich.console import Console, Group
from rich.panel import Panel
from rich.text import Text
from rich.align import Align

console = Console()

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

    console.print(
        Panel(
            Align.center(ascii_art),
            title="[bold white]TuneSort" + "[bold green] v0.1.0",
            title_align="left",
            subtitle="[bold white]Made with" + "[bold #f05d67] ❤" + "[bold white] by" + "[bold #36544F] Jotlz",
            border_style="cyan",
            padding=(2, 1),
            width=110,
            height=15
        )
    )