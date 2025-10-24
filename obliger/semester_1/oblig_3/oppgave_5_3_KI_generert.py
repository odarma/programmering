#måtte kopiere og lime inn movies-listen for at KI-koden skulle fungere
movies = [
    {"name": "Inception", "year": 2010, "rating": 8.7},
    {"name": "Inside Out", "year": 2015, "rating": 8.1},
    {"name": "Con Air", "year": 1997, "rating": 6.9}
]

# A) Funksjon for å skrive filmer til fil
def write_movies_to_file(movie_list, filename):
    with open(filename, 'w') as file:
        for movie in movie_list:
            file.write(f"{movie['name']} - {movie['year']} has a rating of {movie['rating']}\n")

# Skrive til "movies.txt"
write_movies_to_file(movies, "movies.txt")

# B) Funksjon for å lese fra fil
def read_movies_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        print(content)

# Lese fra "movies.txt"
read_movies_from_file("movies.txt")
