import jwt
from fastapi import Header, HTTPException

from app.config import settings


def verify_token(authorization: str = Header(...)):
    try:
        token = authorization.replace("Bearer ", "")
        jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            algorithms=[settings.JWT_ALGORITHM]
        )
        return True
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
