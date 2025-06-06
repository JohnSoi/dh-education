"""Модуль для настроек приложения"""

__author__: str = "Старков Е.П."

from pydantic import Field
from pydantic_settings import BaseSettings
from dh_platform.settings import BaseAppSettings, get_core_settings


class Settings(BaseSettings):
    """
    Класс настроек приложения

    Examples:
          >>> settings.core.DEBUG # Настройка отладки
    """
    core: BaseAppSettings = Field(default_factory=get_core_settings)

    class Config:
        env_nested_delimiter = "__"


settings: Settings = Settings()
