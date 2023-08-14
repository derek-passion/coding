class Movies:
    watched = []
    genre = []
    rating = []
    def list(name, watched, genre, rating):
        name.watched.append(watched)
        name.genre.append(genre)
        name.rating.append(rating)
name = input('Enter a name: ')
movie = Movies()
movie.watched.append(input('Enter a movie: '))
movie.genre.append(input('Enter a genre: '))
movie.rating.append(int(input('Enter a rating: ')))
while movie.rating[-1] > 0:
    movie.watched.append(input('Enter a movie: '))
    movie.genre.append(input('Enter a genre: '))
    movie.rating.append(int(input('Enter a rating: ')))
print(movie.watched, movie.genre, movie.rating)