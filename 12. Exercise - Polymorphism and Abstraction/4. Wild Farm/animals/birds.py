from project.animals.animal import Bird


class Owl(Bird):
    FOOD = ['Meat']
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    @property
    def allowed_foods(self):
        return self.FOOD

    @property
    def weight_add(self):
        return 0.25

class Hen(Bird):
    FOOD = ['Meat', 'Vegetable', 'Fruit', 'Seed']
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    @property
    def allowed_foods(self):
        return self.FOOD

    @property
    def weight_add(self):
        return 0.35