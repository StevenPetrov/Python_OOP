from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, name, weight, food_eaten=0):
        self.name = name
        self.food_eaten = food_eaten
        self.weight = weight

    @abstractmethod
    def make_sound(self):
        pass

    @property
    @abstractmethod
    def allowed_foods(self):
        pass

    @property
    @abstractmethod
    def weight_add(self):
        pass

    def feed(self, food):
        if food.__class__.__name__ not in self.allowed_foods:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += (self.weight_add * food.quantity)
        self.food_eaten += food.quantity



class Bird(Animal):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"