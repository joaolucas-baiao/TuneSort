from tunesort.spotify.biblioteca import Artista, Musica, artistas_unicos


def test_artista_repetido_aparece_uma_vez():
    pitty = Artista(id="1", nome="Pitty")
    cazuza = Artista(id="2", nome="Cazuza")
    musica_a = Musica(uri="spotify:track:a", nome="Máscara", artistas=(pitty,), data_adicao="2024-01-01T00:00:00Z")
    musica_b = Musica(uri="spotify:track:b", nome="Admirável Chip Novo", artistas=(pitty, cazuza), data_adicao="2024-01-02T00:00:00Z")
    resultado = artistas_unicos(musicas=[musica_a, musica_b])
    assert [a.id for a in resultado] == ["1", "2"]


def test_lista_vazia_retorna_lista_vazia():
    resultado = artistas_unicos(musicas=[])
    assert resultado == []


def test_musica_com_dois_artistas():
    xuxa = Artista(id="1", nome="Xuxa")
    pearljam = Artista(id="2", nome="Pearl Jam")

    musica1 = Musica(uri="spotify:track:1", nome="Rock dos baixinhos", artistas=(pearljam, xuxa), data_adicao="2021-06-06T00:00:00Z")

    resultado = artistas_unicos(musicas=[musica1])
    assert [a.nome for a in resultado] == ["Pearl Jam", "Xuxa"]


def test_mesmo_artista_com_nome_diferente():
    racionais1 = Artista("1", "Racionais Mc's")
    racionais2 = Artista("1", "Racionais Mcs")

    musica1 = Musica(uri="spotify:track:2", nome="Homem na Estrada", artistas=(racionais1, racionais2), data_adicao="2021-01-01T00:00:00Z")

    resultado = artistas_unicos(musicas=[musica1])
    assert [a.nome for a in resultado] == ["Racionais Mc's"]