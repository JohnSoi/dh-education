# pylint: disable=no-member
"""Главный файл приложения"""

__author__: str = "Старков Е.П."

from contextlib import asynccontextmanager

from dh_access.initializers import role_init, access_event_subscribe
from dh_access.routes import auth_routes
from dh_contacts.initializers import contacts_event_subscribe
from dh_contacts.routes import contact_routes
from dh_platform.logging import log_requests, setup_logging
from dh_users.routes import user_routes
from fastapi import FastAPI

from dh_education.settings import settings

from .consts import ROLES_DATA


@asynccontextmanager
async def lifespan(_: FastAPI):
    """Жизненный цикл приложения"""
    await role_init(ROLES_DATA)
    access_event_subscribe()
    contacts_event_subscribe()
    setup_logging()
    yield


app: FastAPI = FastAPI(
    title=settings.core.PROJECT_NAME,
    version=settings.core.VERSION,
    debug=settings.core.DEBUG,
    lifespan=lifespan,
)

app.include_router(user_routes)
app.include_router(auth_routes)
app.include_router(contact_routes)
app.middleware("http")(log_requests)
