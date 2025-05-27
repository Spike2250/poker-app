from fastapi import APIRouter

from api.fastapi_users import fastapi_users
from core.schemas.user import (
    UserRead,
    UserUpdate,
)


router = APIRouter(
    tags=["Users"],
)

# /me
# /{id}
router.include_router(
    router=fastapi_users.get_register_router(
        UserRead,
        UserUpdate,
    )
)
