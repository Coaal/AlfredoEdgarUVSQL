import requests

BASE_URL = "http://127.0.0.1:8000"

def get_players():
    r = requests.get(f"{BASE_URL}/players/")
    print(r.json())

def create_player():
    data = {"name": "Test", "level": 1}
    r = requests.post(f"{BASE_URL}/players/", json=data)
    print(r.json())

def get_games():
    r = requests.get(f"{BASE_URL}/games/")
    print(r.json())

def create_game():
    data = {"score": 50, "duration": 20, "player_id": 1}
    r = requests.post(f"{BASE_URL}/games/", json=data)
    print(r.json())

if __name__ == "__main__":
    create_player()
    get_players()
    create_game()
    get_games()