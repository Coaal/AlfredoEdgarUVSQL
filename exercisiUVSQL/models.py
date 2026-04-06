from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

class Player(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    level: int

    games: List["Game"] = Relationship(back_populates="player")


class Game(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    score: int
    duration: int

    player_id: Optional[int] = Field(default=None, foreign_key="player.id")
    player: Optional[Player] = Relationship(back_populates="games")