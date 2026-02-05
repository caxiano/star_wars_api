from app.utils.link_utils import swapi_to_internal


def normalize_species(
    raw_species: list[dict],
    people_index: dict[str, str],
    films_index: dict[str, str],
) -> list[dict]:
    """
    Normaliza espécies da SWAPI, expondo correlações
    com personagens e filmes.
    """
    normalized = []

    # Normalização das espécies
    for specie in raw_species:
        normalized.append({
            "id": int(specie["url"].rstrip("/").split("/")[-1]),
            "name": specie["name"],
            "classification": specie["classification"],
            "language": specie["language"],
            "people": {
                people_index.get(url, "Unknown"): swapi_to_internal(url)
                for url in specie["people"]
            },
            "films": {
                films_index.get(url, "Unknown"): swapi_to_internal(url)
                for url in specie["films"]
            }
        })

    return normalized
