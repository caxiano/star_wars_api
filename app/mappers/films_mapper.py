from app.utils.link_utils import swapi_to_internal


def normalize_films(
    raw_films: list[dict],
    people_index: dict[str, str],
    planets_index: dict[str, str],
    species_index: dict[str, str],
    starships_index: dict[str, str],
    vehicles_index: dict[str, str],
) -> list[dict]:
    """
    Normaliza filmes da SWAPI, retornando todas as correlações
    disponíveis de forma limpa e navegável.
    :param raw_films: Lista de filmes da SWAPI.
    :param people_index: Índice de personagens.
    :param planets_index: Índice de planetas.
    :param species_index: Índice de espécies.
    :param starships_index: Índice de naves espaciais.
    :param vehicles_index: Índice de veículos.
    :return: Lista de filmes normalizados.
    """
    normalized = []

    # Normalização dos filmes
    for film in raw_films:
        normalized.append({
            "id": film["episode_id"],
            "title": film["title"],
            "director": film["director"],
            "producer": film["producer"],
            "release_date": film["release_date"],
            "characters": {
                people_index.get(url, "Unknown"): swapi_to_internal(url)
                for url in film["characters"]
            },
            "planets": {
                planets_index.get(url, "Unknown"): swapi_to_internal(url)
                for url in film["planets"]
            },
            "species": {
                species_index.get(url, "Unknown"): swapi_to_internal(url)
                for url in film["species"]
            },
            "starships": {
                starships_index.get(url, "Unknown"): swapi_to_internal(url)
                for url in film["starships"]
            },
            "vehicles": {
                vehicles_index.get(url, "Unknown"): swapi_to_internal(url)
                for url in film["vehicles"]
            }
        })

    return normalized
