from fastapi import APIRouter

from app.core.security import create_access_token

router = APIRouter()


@router.post("/login")
def login():
    """
    Endpoint fictício apenas para gerar JWT.
    Não há validação de usuário.
    """
    token = create_access_token(
        id="123",
        email="admin@swapi.com",
        role="admin"
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
