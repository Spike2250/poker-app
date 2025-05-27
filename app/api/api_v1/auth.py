from fastapi import APIRouter

from api.dependencies.authentication.backend import authentication_backend
from api.fastapi_users import fastapi_users


router = APIRouter(
    tags=["Auth"],
)
router.include_router(
    router=fastapi_users.get_auth_router(authentication_backend),
)
