from fastapi import APIRouter

from core.config import settings

# from .content import router as content_router

router = APIRouter(
    prefix=settings.api.v1.prefix
)
# router.include_router(
#     content_router,
#     prefix=settings.api.v1.content
# )
