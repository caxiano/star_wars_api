from fastapi import Depends, FastAPI
from fastapi.responses import RedirectResponse

from app.core.auth import get_current_user
from app.lifespan import lifespan
from app.routers import (auth, films, people, planets, species, starships,
                         vehicles)

app = FastAPI(
    lifespan=lifespan,
    title="🌌 Star Wars Explorer 🌌",
    version="2.0.0",
    description=""" 
🚀 **Star Wars Explorer API**

Uma API interativa para explorar o universo de **Star Wars**, utilizando dados da **SWAPI**,
normalizados e enriquecidos para melhor experiência do usuário.

---

### 🔐 Autenticação
Esta API utiliza **JWT (JSON Web Token)**.

1. Faça login em `/auth/login`
2. Copie o token retornado
3. Clique em **Authorize**
4. Use o formato:
Bearer SEU_TOKEN_AQUI


---

### 🌌 Recursos disponíveis
- 👤 Pessoas
- 🪐 Planetas
- 🎬 Filmes
- 🧬 Espécies
- 🚀 Espaçonaves
- 🚗 Veículos
""",
    contact={
        "name": "Cassiano Shigueyuki Nishikawa",
        "email": "csnishikawa@gmail.com",
        "url": "https://github.com/caxiano/starwars-api",
    },
    swagger_ui_parameters={
        "docExpansion": "list",
        "defaultModelsExpandDepth": -1,
        "filter": True,
        "showRequestDuration": True,
        "syntaxHighlight.theme": "obsidian",
    },
)

app.include_router(auth.router, prefix="/auth", tags=["🔐 Autenticação"])
app.include_router(people.router, prefix="/api/people",
                   tags=["👤 Pessoas"], dependencies=[Depends(get_current_user)])
app.include_router(planets.router, prefix="/api/planets",
                   tags=["🪐 Planetas"], dependencies=[Depends(get_current_user)])
app.include_router(films.router, prefix="/api/films",
                   tags=["🎬 Filmes"], dependencies=[Depends(get_current_user)])
app.include_router(species.router, prefix="/api/species",
                   tags=["🧬 Espécies"], dependencies=[Depends(get_current_user)])
app.include_router(starships.router, prefix="/api/starships",
                   tags=["🚀 Espaçonaves"], dependencies=[Depends(get_current_user)])
app.include_router(vehicles.router, prefix="/api/vehicles",
                   tags=["🚗 Veículos"], dependencies=[Depends(get_current_user)])


@app.get("/", include_in_schema=False)
def root():
    """
    Redireciona a raiz do site para a documentação interativa (/docs).
    """
    return RedirectResponse(url="/docs")
