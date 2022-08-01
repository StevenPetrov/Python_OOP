from project.animals.animal import Mammal


class Mouse(Mammal):
    FOOD = ['Vegetables', 'Fruits']

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    @property
    def allowed_foods(self):
        return self.FOOD

    @property
    def weight_add(self):
        return 0.10

class Dog(Mammal):
    FOOD = ['Meat']

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    @property
    def allowed_foods(self):
        return self.FOOD

    @property
    def weight_add(self):
        return 0.40


class Cat(Mammal):
    FOOD = ['Meat', 'Vegetables']

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    @property
    def allowed_foods(self):
        return self.FOOD

    @property
    def weight_add(self):
        return 0.30

class Tiger(Mammal):
    FOOD = ['Meat']

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    @property
    def allowed_foods(self):
        return self.FOOD

    @property
    def weight_add(self):
        return 1
