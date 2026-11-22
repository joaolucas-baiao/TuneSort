from dataclasses import dataclass


@dataclass(frozen=True)
class Artista:
    id: str
    nome: str


@dataclass(frozen=True)
class Musica:
    uri: str
    nome: str
    artistas: tuple[Artista, ...]
    data_adicao: str


def buscar_curtidas(cliente) -> list[Musica]:
    musicas = []
    pagina = cliente.current_user_saved_tracks(limit=50)

    while pagina:
        for item in pagina["items"]:
            faixa = item["track"]
            artistas = tuple(
                Artista(id=a["id"], nome=a["name"])
                for a in faixa["artists"]
            )
            musicas.append(Musica(
                uri=faixa["uri"],
                nome=faixa["name"],
                artistas=artistas,
                data_adicao=item["added_at"]
            ))
        pagina = cliente.next(pagina)

    return musicas


def artistas_unicos(musicas: list[Musica]) -> list[Artista]:
    vistos = {}
    for musica in musicas:
        for artista in musica.artistas:
            if artista.id not in vistos:
                vistos[artista.id] = artista.nome

    return list(vistos.values())


if __name__ == "__main__":
    from tunesort.config import carregar_config
    from tunesort.spotify.auth import criar_cliente

    cfg = carregar_config()
    cliente = criar_cliente(cfg=cfg)
    musicas = buscar_curtidas(cliente=cliente)
    print(len(musicas))

    artistas = artistas_unicos(musicas=musicas)
    print(len(artistas))