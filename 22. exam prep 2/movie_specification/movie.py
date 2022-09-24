import abc

from project.user import User


class Movie(abc.ABC):
    def __init__(self, title: str, year: int, owner: object, age_restriction: int, likes=0):
        self.likes = likes
        self.age_restriction = age_restriction
        self.owner = owner
        self.year = year
        self.title = title

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if not value or not isinstance(value, str):
            raise ValueError('The title cannot be empty string!')
        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if value < 1888 or not isinstance(value, int):
            raise ValueError("Movies weren't made before 1888!")
        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if not isinstance(value, User):
            raise ValueError('The owner must be an object of type User!')
        self.__owner = value

    @abc.abstractmethod
    def details(self):
        pass
