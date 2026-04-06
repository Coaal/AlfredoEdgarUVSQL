from typing import List

from fastapi import FastAPI, Depends
from sqlmodel import Session, select
from database import lifespan, engine, create_db_and_tables
from models import Player, Game

app = FastAPI(lifespan=lifespan)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def root():
    return {"message": "API de Players y Games"}

def get_session():
    with Session(engine) as session:
        yield session



@app.post("/players/")
def create_player(player: Player, session: Session = Depends(get_session)):
    session.add(player)
    session.commit()
    session.refresh(player)
    return player

@app.get("/players/")
def read_players(session: Session = Depends(get_session)):
    players = session.exec(select(Player)).all()
    return players

@app.get("/players/{player_id}")
def read_player(player_id: int, session: Session = Depends(get_session)):
    return session.get(Player, player_id)

@app.delete("/players/{player_id}")
def delete_player(player_id: int, session: Session = Depends(get_session)):
    player = session.get(Player, player_id)
    session.delete(player)
    session.commit()
    return {"ok": True}



@app.post("/games/")
def create_game(game: Game, session: Session = Depends(get_session)):
    session.add(game)
    session.commit()
    session.refresh(game)
    return game

@app.get("/games/")
def read_games(session: Session = Depends(get_session)):
    return session.exec(select(Game)).all()

@app.get("/games/{game_id}")
def read_game(game_id: int, session: Session = Depends(get_session)):
    return session.get(Game, game_id)

@app.delete("/games/{game_id}")
def delete_game(game_id: int, session: Session = Depends(get_session)):
    game = session.get(Game, game_id)
    session.delete(game)
    session.commit()
    return {"ok": True}