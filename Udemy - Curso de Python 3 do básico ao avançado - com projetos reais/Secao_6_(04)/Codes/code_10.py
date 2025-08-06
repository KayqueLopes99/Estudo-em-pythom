import json
import os

NAME_FILE = 'Aula_10.json'

FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), NAME_FILE))

movie: dict = {
    "title": "O Senhor dos Anéis: A Sociedade do Anel",
    "original_title": "The Lord of the Rings: The Fellowship of the Ring",
    "is_movie": True,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
    "budget": None
}

with open(FILE_PATH, 'w', encoding='utf-8') as file:
    json.dump(movie, file, ensure_ascii=False, indent=2)

with open(FILE_PATH, 'r', encoding='utf-8') as file:
    movie_json: str = json.load(file)
    print(movie_json)
