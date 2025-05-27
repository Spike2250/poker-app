import uuid

from fastapi_users import FastAPIUsers

from core.models import User
# from core.types.user_id import UserIdType

from .dependencies.authentication.user_manager import get_user_manager
from .dependencies.authentication.backend import authentication_backend


# fastapi_users = FastAPIUsers[User, UserIdType](
fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [authentication_backend],
)

current_active_user = fastapi_users.current_user(active=True)
current_active_superuser = fastapi_users.current_user(active=True, superuser=True)
