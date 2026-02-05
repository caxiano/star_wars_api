import jwt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.config import settings
from app.schemas.user import User

security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> User:
    """
    Docstring for get_current_user

    :param credentials: Credenciais da autenticação.
    :type credentials: HTTPAuthorizationCredentials
    :return: Instância do usuário autenticado.
    :rtype: User
    """

    token = credentials.credentials

    try:
        # Decodifica o token JWT
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM]
        )
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

    # Retorna o usuário autenticado
    return User(
        id=payload["id"],
        email=payload["email"],
        role=payload.get("role", "user"),
    )
