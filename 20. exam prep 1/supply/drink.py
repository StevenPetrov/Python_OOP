from EXAM_PREP_1.supply.supply import Supply


class Drink(Supply):
    def __init__(self, name):
        super().__init__(name, 15)
