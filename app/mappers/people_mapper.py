from app.utils.link_utils import swapi_to_internal


def normalize_people(
    raw_people: list[dict],
    films_index: dict[str, str],
    planets_index: dict[str, str],
    species_index: dict[str, str],
    starships_index: dict[str, str],
    vehicles_index: dict[str, str],
) -> list[dict]:
    """
    Normaliza personagens da SWAPI, expondo todas as correlações
    em formato legível e com links internos da API.
    :param raw_people: Lista de personagens da SWAPI.
    :param films_index: Índice de filmes.
    :param planets_index: Índice de planetas.
    :param species_index: Índice de espécies.
    :param starships_index: Índice de naves espaciais.
    :param vehicles_index: Índice de veículos.
    :return: Lista de personagens normalizados.
    """
    normalized = []

    # Normalização dos personagens
    for person in raw_people:
        normalized.append({
            "id": int(person["url"].rstrip("/").split("/")[-1]),
            "name": person["name"],
            "height": person["height"],
            "mass": person["mass"],
            "gender": person["gender"],
            "birth_year": person["birth_year"],
            "homeworld": {
                planets_index.get(person["homeworld"], "Unknown"):
                swapi_to_internal(person["homeworld"])
            },
            "films": {
                films_index.get(url, "Unknown"): swapi_to_internal(url)
                for url in person["films"]
            },
            "species": {
                species_index.get(url, "Unknown"): swapi_to_internal(url)
                for url in person["species"]
            },
            "starships": {
                starships_index.get(url, "Unknown"): swapi_to_internal(url)
                for url in person["starships"]
            },
            "vehicles": {
                vehicles_index.get(url, "Unknown"): swapi_to_internal(url)
                for url in person["vehicles"]
            }
        })

    return normalized
