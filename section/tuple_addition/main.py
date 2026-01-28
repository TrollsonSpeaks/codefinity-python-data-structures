animal_movies = ('The Lion King', 'Jurassic Park', 'Finding Nemo')

# Convert the tuple to a list
movie_list = list(animal_movies)

# Add new movies to the list
movie_list.append("Dumbo")
movie_list.append("Zootopia")

# Convert the list back to a tuple
animal_movies = tuple(movie_list)

print("Updated animal movies:", animal_movies)