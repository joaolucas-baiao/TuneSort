from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

from tunesort.config import Config, carregar_config


def criar_cliente(cfg: Config):
    cliente = Spotify(
        auth_manager=SpotifyOAuth(
            client_id=cfg.client_id,
            client_secret=cfg.client_secret,
            redirect_uri=cfg.redirect_uri,
            scope=("user-library-read", "playlist-modify-private", "playlist-modify-public")
        )
    )
    return cliente

if __name__ == "__main__":
    cfg = carregar_config()
    cliente = criar_cliente(cfg)
