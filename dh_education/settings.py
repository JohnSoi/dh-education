"""Модуль для настроек приложения"""

__author__: str = "Старков Е.П."

from pydantic import Field
from pydantic_settings import BaseSettings
from dh_platform.settings import *
from dh_access.settings import *


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
        env_file = ".env"
        extra = "ignore"


settings: Settings = Settings()
