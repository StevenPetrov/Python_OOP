import os


class User:
    def __init__(self, username: str, age: int):
        self.age = age
        self.username = username
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Invalid username")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = value

    def __str__(self):
        liked_movies = "No movies liked."
        if self.movies_liked:
            liked_movies = os.linesep.join(x.details() for x in self.movies_liked)
        movies_owned = "No movies owned."
        if self.movies_owned:
            movies_owned = os.linesep.join(x.details() for x in self.movies_owned)

        return f"Username: {self.username}, Age: {self.age}"\
"Liked movies:" \
f"{liked_movies}"\
"Owned movies:"\
f"{movies_owned}"

