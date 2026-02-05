from app.mappers.films_mapper import normalize_films
from app.mappers.people_mapper import normalize_people
from app.mappers.planets_mapper import normalize_planets
from app.mappers.species_mapper import normalize_species
from app.mappers.starships_mapper import normalize_starships
from app.mappers.vehicles_mapper import normalize_vehicles
from app.services.json_store import save_json
from app.services.swapi_ingest import fetch_all_pages


async def bootstrap_data() -> None:
    """
    Realiza o carregamento inicial da aplicação.

    Responsabilidades:
    - Buscar todos os dados da SWAPI (sem paginação)
    - Criar índices globais (url -> nome/título)
    - Normalizar os dados removendo campos desnecessários
    - Converter links externos em links internos da API
    - Persistir os dados finais em arquivos JSON locais

    Essa função é executada automaticamente no startup da aplicação.
    """

    # =========================
    # 1. INGESTÃO DOS DADOS
    # =========================

    raw_people = await fetch_all_pages("people")
    raw_films = await fetch_all_pages("films")
    raw_planets = await fetch_all_pages("planets")
    raw_species = await fetch_all_pages("species")
    raw_starships = await fetch_all_pages("starships")
    raw_vehicles = await fetch_all_pages("vehicles")

    # =========================
    # 2. CRIAÇÃO DOS ÍNDICES
    # =========================
    # Usados para substituir URLs por nomes/títulos legíveis

    people_index = {people["url"]: people["name"] for people in raw_people}
    films_index = {film["url"]: film["title"] for film in raw_films}
    planets_index = {planet["url"]: planet["name"] for planet in raw_planets}
    species_index = {specie["url"]: specie["name"] for specie in raw_species}
    starships_index = {starship["url"]: starship["name"]
                       for starship in raw_starships}
    vehicles_index = {vehicle["url"]: vehicle["name"]
                      for vehicle in raw_vehicles}

    # =========================
    # 3. NORMALIZAÇÃO
    # =========================

    people = normalize_people(
        raw_people,
        films_index,
        planets_index,
        species_index,
        starships_index,
        vehicles_index,
    )

    films = normalize_films(
        raw_films,
        people_index,
        planets_index,
        species_index,
        starships_index,
        vehicles_index,
    )

    planets = normalize_planets(
        raw_planets,
        people_index,
        films_index,
    )

    species = normalize_species(
        raw_species,
        people_index,
        films_index,
    )

    starships = normalize_starships(
        raw_starships,
        people_index,
        films_index,
    )

    vehicles = normalize_vehicles(
        raw_vehicles,
        people_index,
        films_index,
    )

    # =========================
    # 4. PERSISTÊNCIA LOCAL
    # =========================

    save_json("people", people)
    save_json("films", films)
    save_json("planets", planets)
    save_json("species", species)
    save_json("starships", starships)
    save_json("vehicles", vehicles)
