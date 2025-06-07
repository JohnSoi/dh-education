"""Главный файл приложения"""

__author__: str = "Старков Е.П."

from contextlib import asynccontextmanager

from fastapi import FastAPI
from dh_education.settings import settings

from dh_access.initializers import role_init

from .consts import ROLES_DATA


@asynccontextmanager
async def lifespan(_: FastAPI):
    await role_init(ROLES_DATA)

    yield

app: FastAPI = FastAPI(
    title=settings.core.PROJECT_NAME,
    version=settings.core.VERSION,
    debug=settings.core.DEBUG,
    lifespan=lifespan,
)
