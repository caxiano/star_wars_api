from fastapi import FastAPI

from app.routers import films, people
from app.routers.root import router as root_router

app = FastAPI(
    title="🌌 Star Wars Interactive API",
    description="An interactive API to explore the Star Wars universe using data from the SWAPI (Star Wars API).",
    version="1.0.0",
)

app.include_router(root_router)
app.include_router(people.router, prefix="/people", tags=["People"])
app.include_router(people.router, prefix="/planets", tags=["Planets"])
app.include_router(films.router, prefix="/films", tags=["Films"])
app.include_router(people.router, prefix="/species", tags=["Species"])
app.include_router(people.router, prefix="/starships", tags=["Starships"])
app.include_router(people.router, prefix="/vehicles", tags=["Vehicles"])
