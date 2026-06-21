import os
import json

FILENAME = "movies.json"

def load_movies():
    if not os.path.exists(FILENAME):
        return []
    
    with open(FILENAME, "r", encoding="utf-8") as f:
        return json.load(f)
    
    
def save_movies(movies):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(movies, f, indent=2)
        

def add_movie(movies):
    title = input("enter the movie name : ").strip().lower()
    
    if any(movie["title"].lower() == title for movie in movies):
        print("Movie alraedy exists")
        return

    genre = input("Genre : ").strip().lower()
    
    try:
        rating = float(input("Enter rating (0 - 10)"))
        if not (0 <= rating <= 10):
            raise ValueError
    except ValueError:
        print("Please enter valid number")
        return
    
    movies.append({"title" : title, "genre" : genre, "rating" : rating})
    
    save_movies(movies)
    
    print("Movie Added\n")
        
    
def search_movie(movies):
    term = input("Enter the title or genre : ").strip().lower()


movies = load_movies()

add_movie(movies)