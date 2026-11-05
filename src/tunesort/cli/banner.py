from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def mostrar_banner():
    banner = Text(justify="center")
    banner.append("  ████████╗██╗   ██╗███╗   ██╗███████╗███████╗ ██████╗ ██████╗ ████████╗\n", style="bold #0B8185")
    banner.append("  ╚══██╔══╝██║   ██║████╗  ██║██╔════╝██╔════╝██╔═══██╗██╔══██╗╚══██╔══╝\n", style="bold #0B8185")
    banner.append("     ██║   ██║   ██║██╔██╗ ██║█████╗  ███████╗██║   ██║██████╔╝   ██║   \n", style="bold #0B8185")
    banner.append("     ██║   ██║   ██║██║╚██╗██║██╔══╝  ╚════██║██║   ██║██╔══██╗   ██║   \n", style="bold #0B8185")
    banner.append("     ██║   ╚██████╔╝██║ ╚████║███████╗███████║╚██████╔╝██║  ██║   ██║   \n", style="bold #1F5F61")
    banner.append("     ╚═╝    ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   \n", style="bold #1F5F61")

    subtitulo = Text("• Descrição", style="bold white", justify="center")
    subtitulo.append("  -  ", style="bold dim")
    subtitulo.append("Ferramenta CLI para organizar músicas e automatizar playlists do Spotify.", style="bold #85aab0")

    container = Text()
    container.append(banner)
    container.append("\n")
    container.append(subtitulo)

    console.print(
        Panel(
            container,
            title="[bold white]TuneSort" + "[bold green] v0.1.0",
            subtitle="[bold white]Made with" + "[bold #f05d67] ❤" + "[bold white] by" + "[bold #36544F] Jotlz",
            border_style="cyan",
            padding=(1, 2),

        )
    )