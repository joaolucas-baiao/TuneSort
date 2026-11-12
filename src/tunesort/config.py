from dataclasses import dataclass, field
from os import getenv

from dotenv import load_dotenv

load_dotenv()

class ConfigError(Exception):
    """Mensagem de erro de erro própria"""

@dataclass(frozen=True)
class Config:
    client_id: str
    client_secret: str = field(repr=False)
    redirect_uri: str
    last_fm_api_key: str = field(repr=False)

CAMPOS_OBRIGATORIOS = ["CLIENT_ID", "CLIENT_SECRET", "REDIRECT_URI", "LAST_FM_API_KEY"]

def carregar_config():
    val_faltando = []
    val_validos = {}
    for campo in CAMPOS_OBRIGATORIOS:
        valor = getenv(campo)
        if not valor or not valor.strip():
            val_faltando.append(campo)
        else:
            val_validos[campo] = valor.strip()
    if val_faltando:
        raise ConfigError("Campos faltando: " + ", ".join(val_faltando) + "\nConfira se o arquivo '.env' está corretamente preenchido")
    return Config(
        client_id=val_validos['CLIENT_ID'],
        client_secret=val_validos['CLIENT_SECRET'],
        redirect_uri=val_validos['REDIRECT_URI'],
        last_fm_api_key=val_validos['LAST_FM_API_KEY']
    )