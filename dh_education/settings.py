# pylint: disable=wildcard-import
"""Модуль для настроек приложения"""

__author__: str = "Старков Е.П."

from dh_access.settings import AccessSettings, get_access_settings
from dh_platform.settings import *
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Класс настроек приложения

    Examples:
          >>> settings.core.DEBUG # Настройка отладки
    """

    core: BaseAppSettings = Field(default_factory=get_core_settings)
    db: DatabaseSettings = Field(default_factory=get_db_settings)
    access: AccessSettings = Field(default_factory=get_access_settings)

    class Config:
        """Конфиг"""
        env_file = ".env"
        extra = "ignore"


settings: Settings = Settings()
