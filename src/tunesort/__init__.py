import importlib.metadata

try:
    __version__ = importlib.metadata.version('tunesort')
except importlib.metadata.PackageNotFoundError:
    __version__ = "0"