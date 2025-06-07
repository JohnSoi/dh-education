"""Константы модуля"""

__author__: str = "Старков Е.П."

from dh_access.consts import PermissionAccessLevel
from dh_access.types import RolesData

# Базовые роли системы
ROLES_DATA: RolesData = {
    "ADMIN": {
        "permissions": {"users": PermissionAccessLevel.DELETE},
        "description": "Роль с полным доступом в систему. "
        "Может просматривать все сущности и производить все операции над ними",
    },
    "MANAGER": {
        "permissions": {"users": PermissionAccessLevel.DENIED},
        "description": "Управление клиентской базой и учебным процессом в рамках своего филиала",
    },
    "TEACHER": {
        "permissions": {"users": PermissionAccessLevel.DENIED},
        "description": "Проведение занятий и просмотр только своих групп и предметов",
    },
    "STUDENT": {
        "permissions": {"users": PermissionAccessLevel.DENIED},
        "description": "Просмотр расписания, занятий, предметов, материалов в рамках своего курса",
    },
    "DIRECTOR": {
        "permissions": {"users": PermissionAccessLevel.DENIED},
        "description": "Просмотр всех данных в рамках своего филиала",
    },
}
