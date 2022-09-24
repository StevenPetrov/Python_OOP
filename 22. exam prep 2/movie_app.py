import os

from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        if self.get_user_by_username(username):
            raise Exception("User already exists!")
        user = User(username, age)
        self.users_collection.append(user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        user = self.get_user_by_username(username)
        if user is None:
            raise Exception("This user does not exist!")
        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")
        self.movies_collection.append(movie)
        user.movies_owned.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        if movie not in self.movies_collection:
            raise Exception(f'The movie {movie.title} is not uploaded!')
        for key, value in kwargs.items():
            #movie.title - kwargs.get('title', movie.title)
            if key == 'title':
                movie.title = value
            elif key == 'year':
                movie.year = value
            elif key == 'age_restriction':
                movie.age_restriction = value
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = self.get_user_by_username(username)
        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        if movie not in self.movies_collection:
            raise Exception(f'The movie {movie.title} is not uploaded!')
        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self.get_user_by_username(username)
        if movie.owner.username == username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")
        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.get_user_by_username(username)
        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")
        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return f"No movies found."
        sorted_movies = sorted(self.movies_collection, key=self.__movie_order)
        return os.linesep.join(x.details() for x in sorted_movies)

    def __str__(self):
        result = ''
        if not self.users_collection:
            result += "All users: No users."
        else:
            result += f"All users: {', '.join(x.username for x in self.users_collection)}" + '\n'
        if not self.movies_collection:
            result += "All movies: No movies."
        else:
            result += f"All movies: {', '.join(x.title for x in self.movies_collection)}"
        return result

    def get_user_by_username(self, username):
        for user in self.users_collection:
            if user.username == username:
                return user

    @staticmethod
    def __movie_order(movie: Movie):
        return -movie.year, movie.title
