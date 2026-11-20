# Movie Watchlist using python programming language 

movies = []

count = int(input("How many movies do you want to add? "))

for i in range(count):
    movie = input("Enter movie name: ")
    movies.append(movie)

print("\nYour Movie Watchlist:")

for movie in movies:
    print("-", movie)

print("Total movies:", len(movies))