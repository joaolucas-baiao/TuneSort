from dataclasses import dataclass


@dataclass(frozen=True)
class Tag:
    nome: str
    peso: int