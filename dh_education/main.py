"""Главный файл приложения"""

__author__: str = "Старков Е.П."

from fastapi import FastAPI
from dh_education.settings import settings

app: FastAPI = FastAPI(
    title=settings.core.PROJECT_NAME,
    version=settings.core.VERSION,
    debug=settings.core.DEBUG,
)
