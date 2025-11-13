import json
from pathlib import Path
from contextlib import contextmanager

chess_players = [
    {'id': 19, 'name': 'Jobava', 'country': 'Georgia', 'rating': 2588, 'age': 41},
    {'id': 28, 'name': 'Caruana', 'country': 'USA', 'rating': 2781, 'age': 32},
    {'id': 35, 'name': 'Giri', 'country': 'Netherlands', 'rating': 2771, 'age': 30},
    {'id': 84, 'name': 'Carlsen', 'country': 'Norway', 'rating': 2864, 'age': 34},
    {'id': 118, 'name': 'Ding', 'country': 'China', 'rating': 2799, 'age': 32},
    {'id': 139, 'name': 'Karjakin', 'country': 'Russia', 'rating': 2747, 'age': 35},
    {'id': 258, 'name': 'Duda', 'country': 'Poland', 'rating': 2731, 'age': 31},
    {'id': 301, 'name': 'Vachier-Lagrave', 'country': 'France', 'rating': 2737, 'age': 34},
    {'id': 403, 'name': 'Nakamura', 'country': 'USA', 'rating': 2768, 'age': 36},
]

# 1
@contextmanager
def create_file(folder_path, filename):
        file_path = Path(folder_path) / filename
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, 'w') as f:
                yield f

# 2
def read_file(file_path):
        with open(file_path, 'r') as f:
                return json.load(f)

# 3
def append_to_file(file_path, player_dict):
        data = read_file(file_path)
        data.append(player_dict)
        update_file(file_path, data)

# 4
def update_file(file_path, data):
        with open(file_path, 'w') as f:
                json.dump(data, f, indent=2)


if __name__ == "__main__":
        with create_file('.', 'players.json') as f:
                json.dump(chess_players, f, indent=2)
        
        append_to_file('players.json', {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56})
        append_to_file('players.json', {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59})
        
        print(read_file('players.json'))