from project.movie_specification.movie import Movie
from project.user import User


class Thriller(Movie):
    def __init__(self, title: str, year: int, owner: User, age_restriction: int=0):
        super().__init__(title, year, owner, age_restriction=0)
        self.age_restriction = age_restriction

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value == 0:
            self.__age_restriction = 16
            return
        if value < 16:
            raise ValueError('Thriller movies must be restricted for audience under 16 years!')
        self.__age_restriction = value

    def details(self):
        return f"Thriller - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, Likes:{self.likes}, Owned by:{self.owner.username}"