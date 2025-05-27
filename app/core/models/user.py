from fastapi_users.db import (
    # SQLAlchemyBaseUserTableUUID,
    SQLAlchemyBaseUserTable,
    SQLAlchemyUserDatabase,
)

from .base import Base
from .mixins.int_id_pk import IntIdPkMixin


# class User(Base, SQLAlchemyBaseUserTableUUID):
#     pass


class User(Base, IntIdPkMixin, SQLAlchemyBaseUserTable[int]):
    pass
