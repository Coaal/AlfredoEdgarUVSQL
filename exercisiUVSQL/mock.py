from sqlmodel import Session
from database import engine, create_db_and_tables
from models import Player, Game

def create_mock_data():
    create_db_and_tables()

    with Session(engine) as session:
        p1 = Player(name="Alfredo", level=10)
        p2 = Player(name="Edgar", level=5)

        session.add(p1)
        session.add(p2)
        session.commit()

        g1 = Game(score=100, duration=30, player_id=p1.id)
        g2 = Game(score=200, duration=45, player_id=p1.id)

        session.add(g1)
        session.add(g2)
        session.commit()

if __name__ == "__main__":
    create_mock_data()