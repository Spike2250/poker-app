from core.schemas.user import (
    UserCreate,
    UserRead,
    UserUpdate,
)
from core.config import settings


PREFIX = settings.api.prefix + settings.api.v1.prefix
USER_CREATE_VALID = UserCreate(
    email="bob@mail.com",
    password="qwerty123",
)
USER_CREATE_SUPERUSER_VERIFIED = UserCreate(
    email="mark@mail.com",
    password="ytrewq321",
    is_active=True,
    is_superuser=True,
    is_verified=True,
)
