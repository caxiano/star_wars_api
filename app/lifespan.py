from contextlib import asynccontextmanager

from fastapi import FastAPI

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
    await bootstrap_data()

    yield
