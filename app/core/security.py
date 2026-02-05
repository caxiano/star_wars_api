from datetime import datetime, timedelta, timezone

import jwt

from app.config import settings


def create_access_token(
    id: str,
    email: str,
    role: str,
    expires_minutes: int = 60,
) -> str:
    """
    Cria um token JWT assinado para autenticação do usuário.

    :param id: Identificador único do usuário
    :param email: Email do usuário autenticado
    :param role: Papel do usuário no sistema
    :param expires_minutes: Tempo de expiração do token em minutos
    :return: Token JWT assinado
    """

    payload = {
        "id": id,
        "email": email,
        "role": role,
        "exp": datetime.now(timezone.utc) + timedelta(
            minutes=settings.JWT_EXPIRE_MINUTES or expires_minutes
        ),
    }

    return jwt.encode(
        payload,
        settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM,
    )
