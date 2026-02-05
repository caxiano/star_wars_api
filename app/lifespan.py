from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config import settings
from app.services.bootstrap import bootstrap_data


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Docstring for lifespan

    :param app: app instance
    :type app: FastAPI
    :yield: None
    """
    # STARTUP
    if not settings.TESTING:
        await bootstrap_data()

    yield
