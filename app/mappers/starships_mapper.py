from app.utils.link_utils import swapi_to_internal


def normalize_starships(
    raw_starships: list[dict],
    people_index: dict[str, str],
    films_index: dict[str, str],
) -> list[dict]:
    """
    Normaliza naves espaciais da SWAPI, incluindo
    pilotos e filmes relacionados.
    """
    normalized = []

    # Normalização das naves espaciais
    for ship in raw_starships:
        normalized.append({
            "id": int(ship["url"].rstrip("/").split("/")[-1]),
            "name": ship["name"],
            "model": ship["model"],
            "manufacturer": ship["manufacturer"],
            "pilots": {
                people_index.get(url, "Unknown"): swapi_to_internal(url)
                for url in ship["pilots"]
            },
            "films": {
                films_index.get(url, "Unknown"): swapi_to_internal(url)
                for url in ship["films"]
            }
        })

    return normalized
