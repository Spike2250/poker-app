from typing import TYPE_CHECKING

from fastapi_users.db import (
    # SQLAlchemyBaseUserTableUUID,
    SQLAlchemyBaseUserTable,
    SQLAlchemyUserDatabase,
)

from .base import Base
from .mixins.int_id_pk import IntIdPkMixin

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

# class User(Base, SQLAlchemyBaseUserTableUUID):
#     pass


class User(Base, IntIdPkMixin, SQLAlchemyBaseUserTable[int]):

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, User)
