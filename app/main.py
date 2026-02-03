from fastapi import Depends, FastAPI

from app.core.auth import get_current_user
from app.routers import (auth, films, people, planets, species, starships,
                         vehicles)

app = FastAPI(
    title="🌌 Star Wars Explorer 🌌",
    summary="Explore o universo de Star Wars com dados da SWAPI",
    description=f"""
        Uma API interativa para explorar o universo de Star Wars usando dados da SWAPI (Star Wars API).
        Esta API permite ao usuário acessar informações sobre personagens, planetas, espaçonaves, veículos, espécies e filmes da franquia Star Wars.
        É construída com FastAPI e fornece autenticação baseada em JWT para acesso seguro aos endpoints.""",
    version="1.0.0",
    contact={
        "name": "Cassiano Shigueyuki Nishikawa",
        "email": "csnishikawa@gmail.com",
        "url": "https://github.com/caxiano/starwars-api",

    },
)

app.include_router(auth.router, prefix="/auth", tags=["Autenticação"])
app.include_router(people.router, prefix="/people",
                   tags=["Pessoas"], dependencies=[Depends(get_current_user)])
app.include_router(planets.router, prefix="/planets",
                   tags=["Planetas"], dependencies=[Depends(get_current_user)])
app.include_router(films.router, prefix="/films",
                   tags=["Filmes"], dependencies=[Depends(get_current_user)])
app.include_router(species.router, prefix="/species",
                   tags=["Espécies"], dependencies=[Depends(get_current_user)])
app.include_router(starships.router, prefix="/starships",
                   tags=["Espaçonaves"], dependencies=[Depends(get_current_user)])
app.include_router(vehicles.router, prefix="/vehicles",
                   tags=["Veículos"], dependencies=[Depends(get_current_user)])
