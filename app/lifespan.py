from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config import settings
from app.services.bootstrap import bootstrap_data
from app.services.json_store import clear_data_dir


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
        if settings.FORCE_REBUILD_DATA:
            clear_data_dir()
        await bootstrap_data()

    yield
