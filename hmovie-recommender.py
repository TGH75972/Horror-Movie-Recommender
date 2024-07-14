import random

class Movie:
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating

class MovieRecommender:
    def __init__(self):
        self.movies = []
    
    def add_movie(self, title, director, rating):
        self.movies.append(Movie(title, director, rating))
    
    def recommend_movies(self, min_rating=4.0, num_movies=5):
        filtered_movies = [movie for movie in self.movies if movie.rating >= min_rating]
        recommended_movies = random.sample(filtered_movies, min(num_movies, len(filtered_movies)))
        return recommended_movies
    
    def list_movies(self):
        return self.movies

movie_recommender = MovieRecommender()
movie_recommender.add_movie('The Exorcist', 'William Friedkin', 4.5)
movie_recommender.add_movie('The Shining', 'Stanley Kubrick', 4.6)
movie_recommender.add_movie('Psycho', 'Alfred Hitchcock', 4.4)
movie_recommender.add_movie('Halloween', 'John Carpenter', 4.3)
movie_recommender.add_movie('A Nightmare on Elm Street', 'Wes Craven', 4.2)
movie_recommender.add_movie('The Texas Chain Saw Massacre', 'Tobe Hooper', 4.1)
movie_recommender.add_movie('Hereditary', 'Ari Aster', 4.1)
movie_recommender.add_movie('The Conjuring', 'James Wan', 4.3)
movie_recommender.add_movie('Get Out', 'Jordan Peele', 4.4)
movie_recommender.add_movie('It Follows', 'David Robert Mitchell', 4.0)
movie_recommender.add_movie('The Babadook', 'Jennifer Kent', 4.2)
movie_recommender.add_movie('The Witch', 'Robert Eggers', 4.3)
movie_recommender.add_movie('Paranormal Activity', 'Oren Peli', 4.0)
movie_recommender.add_movie('Insidious', 'James Wan', 4.1)
movie_recommender.add_movie('Sinister', 'Scott Derrickson', 4.2)
movie_recommender.add_movie('Carrie', 'Brian De Palma', 4.3)
movie_recommender.add_movie('The Ring', 'Gore Verbinski', 4.0)
movie_recommender.add_movie('The Blair Witch Project', 'Daniel Myrick', 4.1)
movie_recommender.add_movie('Poltergeist', 'Tobe Hooper', 4.2)
movie_recommender.add_movie('Scream', 'Wes Craven', 4.1)
movie_recommender.add_movie('The Sixth Sense', 'M. Night Shyamalan', 4.5)
movie_recommender.add_movie('28 Days Later', 'Danny Boyle', 4.2)
movie_recommender.add_movie('Let the Right One In', 'Tomas Alfredson', 4.4)
movie_recommender.add_movie('The Cabin in the Woods', 'Drew Goddard', 4.0)
movie_recommender.add_movie('Saw', 'James Wan', 4.1)
movie_recommender.add_movie('The Omen', 'Richard Donner', 4.3)
movie_recommender.add_movie('The Others', 'Alejandro Amenábar', 4.1)
movie_recommender.add_movie('The Fly', 'David Cronenberg', 4.2)
movie_recommender.add_movie('Child\'s Play', 'Tom Holland', 4.0)
movie_recommender.add_movie('An American Werewolf in London', 'John Landis', 4.1)
movie_recommender.add_movie('Evil Dead II', 'Sam Raimi', 4.2)
movie_recommender.add_movie('Night of the Living Dead', 'George A. Romero', 4.3)
movie_recommender.add_movie('The Silence of the Lambs', 'Jonathan Demme', 4.6)
movie_recommender.add_movie('Rosemary\'s Baby', 'Roman Polanski', 4.4)
movie_recommender.add_movie('Jaws', 'Steven Spielberg', 4.3)
movie_recommender.add_movie('The Thing', 'John Carpenter', 4.6)
movie_recommender.add_movie('Smile', 'Parker Finn', 4.0)
movie_recommender.add_movie('Ju-on: The Grudge', 'Takashi Shimizu', 4.2)
movie_recommender.add_movie('Texas Chainsaw Massacre', 'Tobe Hooper', 4.1)
movie_recommender.add_movie('Candyman', 'Bernard Rose', 4.0)

while True:
    command = input("Enter command (recommend, list, exit): ").strip().lower()
    if command == 'recommend':
        min_rating = float(input("Minimum rating (default 4.0): ").strip() or 4.0)
        num_movies = int(input("Number of movies (default 5): ").strip() or 5)
        recommendations = movie_recommender.recommend_movies(min_rating, num_movies)
        for movie in recommendations:
            print(f"{movie.title} directed by {movie.director} (Rating: {movie.rating})")
    elif command == 'list':
        movies = movie_recommender.list_movies()
        for movie in movies:
            print(f"{movie.title} directed by {movie.director} (Rating: {movie.rating})")
    elif command == 'exit':
        break
    else:
        print("Invalid command.")
