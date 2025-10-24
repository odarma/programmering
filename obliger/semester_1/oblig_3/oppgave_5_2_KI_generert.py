#måtte kopiere og lime inn movies-listen for at KI-koden skulle fungere
movies = [
    {"name": "Inception", "year": 2010, "rating": 8.7},
    {"name": "Inside Out", "year": 2015, "rating": 8.1},
    {"name": "Con Air", "year": 1997, "rating": 6.9}
]

# A) Funksjon for å printe ut alle filmer i en gitt liste
def print_movies(movie_list):
    for movie in movie_list:
        print(f"{movie['name']} - {movie['year']} has a rating of {movie['rating']}")

print_movies(movies)

# B) Funksjon for å regne ut gjennomsnittsrating
def average_rating(movie_list):
    total_rating = sum(movie['rating'] for movie in movie_list)
    average = total_rating / len(movie_list)
    return average

avg = average_rating(movies)
print(f"Average rating: {avg}")

# C) Funksjon for å returnere filmer fra og med et gitt årstall
def movies_from_year(movie_list, year):
    return [movie for movie in movie_list if movie['year'] >= year]

# Benytte funksjonen og printe ut filmen fra og med 2010
movies_since_2010 = movies_from_year(movies, 2010)
print_movies(movies_since_2010)
