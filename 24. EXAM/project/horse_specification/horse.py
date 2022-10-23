import abc


class Horse(abc.ABC):
    def __init__(self, name: str, speed: int, is_taken=False):
        self.name = name
        self.speed = speed
        self.is_taken = is_taken

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 4 or not isinstance(value, str):
            raise ValueError(f"Horse name {value} is less than 4 symbols!")
        self.__name = value

    # @property
    # def speed(self):
    #     return self.__speed
    #
    # @speed.setter
    # def speed(self, value):
    #
    #     self.__speed = value
    @abc.abstractmethod
    def train(self):
        pass