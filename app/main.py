from fastapi import Depends, FastAPI

from app.core.auth import get_current_user
from app.routers import (auth, films, people, planets, species, starships,
                         vehicles)

app = FastAPI(
    title="🌌 Star Wars Explorer 🌌",
    contact={
        "name": "Cassiano Shigueyuki Nishikawa",
        "email": "csnishikawa@gmail.com",
        "url": "https://github.com/caxiano/starwars-api",

    },
    description=f"""
        An interactive API to explore the Star Wars universe using data from the SWAPI (Star Wars API).
        This API allows users to access information about characters, planets, starships, vehicles, species, and films from the Star Wars franchise.
        It is built with FastAPI and provides JWT-based authentication for secure access to the endpoints.""",
    version="1.0.0",
)

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
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
