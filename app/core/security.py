from datetime import datetime, timedelta

import jwt

from app.config import settings


def create_access_token(
    id: str,
    email: str,
    role: str = "user",
    expires_minutes: int | None = None
) -> str:
    expire = datetime.utcnow() + timedelta(
        minutes=expires_minutes or settings.JWT_EXPIRE_MINUTES
    )

    payload = {
        "id": id,
        "email": email,
        "role": role,
        "exp": expire
    }

    return jwt.encode(
        payload,
        settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM
    )
