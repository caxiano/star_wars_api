import time

_CACHE: dict[str, tuple[float, dict]] = {}
TTL = 3600


def get_from_cache(key: str):
    if key not in _CACHE:
        return None

    expires_at, value = _CACHE[key]
    if time.time() > expires_at:
        del _CACHE[key]
        return None

    return value


def set_cache(key: str, value: dict):
    _CACHE[key] = (time.time() + TTL, value)
