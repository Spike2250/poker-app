from pydantic import BaseModel
from enum import Enum
from uuid import UUID
from .card import Card


class CommonStatus(str, Enum):
    ACTIVE = "active"
    AFK = "afk"
    WATCHER = "watcher"


class GameStatus(str, Enum):
    EMPTY = 'empty'
    IN_GAME = "in_game"
    FOLDED = "folded"


class Player(BaseModel):
    id: UUID
    nickname: str
    stack: int | None = None
    hand: list[Card] | None = None
    board_place: int | None = None
    time_bank: int | None = None
    common_status: CommonStatus = CommonStatus.ACTIVE
    game_status: GameStatus = GameStatus.EMPTY
