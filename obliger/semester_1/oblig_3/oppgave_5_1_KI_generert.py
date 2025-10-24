# A) Opprett en liste med filmer
movies = [
    {"name": "Inception", "year": 2010, "rating": 8.7},
    {"name": "Inside Out", "year": 2015, "rating": 8.1},
    {"name": "Con Air", "year": 1997, "rating": 6.9}
]

# B) Opprett en funksjon som legger til en film
def add_movie(movie_list, name, year, rating=None):
    if rating is None:
        rating = 5.0  # Default rating
    movie = {"name": name, "year": year, "rating": rating}
    movie_list.append(movie)

# Legg til 3 nye filmer
add_movie(movies, "The Lion King", 1994, 8.5)
add_movie(movies, "The Matrix", 1999, 8.7)
add_movie(movies, "Interstellar", 2014, 8.6)

# C) Modifiser funksjonen for default-rating
add_movie(movies, "Zootopia", 2016)  # Ingen rating spesifisert

#måtte skrive denne selv for å sjekke kjørbarheten
print(movies)