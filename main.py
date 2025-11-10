import os
import json
from typing import Union, List, Dict

# main.py

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

#1
def create_file(directory: str, filename: str) -> None:
    file_path = os.path.join(directory, filename)
    try:
        with open(file_path, 'w') as f:
            pass  # Creates empty file
    except OSError as e:
        print(f"Error creating file: {e}")

#2
def read_file(file_path: str) -> Union[str, None]:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except OSError as e:
        print(f"Error reading file {file_path}: {e}")
    return None

#3
def append_dict_to_file(data: Dict, file_path: str) -> None:
    try:
        dirpath = os.path.dirname(file_path)
        if dirpath:
            os.makedirs(dirpath, exist_ok=True)
        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(json.dumps(data, ensure_ascii=False) + '\n')
    except (TypeError, ValueError) as e:
        print(f"Error serializing data to JSON: {e}")
    except OSError as e:
        print(f"Error writing to file {file_path}: {e}")