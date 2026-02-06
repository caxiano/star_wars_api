import json
import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def ensure_data_dir() -> None:
    """
    Garante que o diretório de dados exista.
    """
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def clear_data_dir() -> None:
    """
    Remove o diretório /data para forçar a recriação.
    """
    shutil.rmtree(DATA_DIR, ignore_errors=True)


def get_json_path(resource: str) -> Path:
    """
    Retorna o caminho do arquivo JSON de um recurso.

    :param resource: Nome do recurso (ex: people, films)
    :return: Caminho do arquivo JSON
    """
    ensure_data_dir()
    return DATA_DIR / f"{resource}.json"


def load_json(resource: str) -> list[dict]:
    """
    Carrega os dados de um arquivo JSON.

    :param resource: Nome do recurso
    :return: Lista de registros ou lista vazia se não existir
    """
    path = get_json_path(resource)

    if not path.exists():
        return []

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_json(resource: str, data: list[dict]) -> None:
    """
    Salva dados normalizados em um arquivo JSON.

    :param resource: Nome do recurso
    :param data: Lista de registros normalizados
    """
    path = get_json_path(resource)

    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
