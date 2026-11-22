from tunesort.spotify.biblioteca import Artista, Musica, artistas_unicos


def test_artista_repetido_aparece_uma_vez():
    pitty = Artista(id="1", nome="Pitty")
    cazuza = Artista(id="2", nome="Cazuza")
    musica_a = Musica(uri="spotify:track:a", nome="Máscara", artistas=(pitty,), data_adicao="2024-01-01T00:00:00Z")
    musica_b = Musica(uri="spotify:track:b", nome="Admirável Chip Novo", artistas=(pitty, cazuza), data_adicao="2024-01-02T00:00:00Z")
    resultado = artistas_unicos(musicas=[musica_a, musica_b])
    assert [a.id for a in resultado] == ["1", "2"]