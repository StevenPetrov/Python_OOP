import unittest

from car_manager import Car


class CarTest(unittest.TestCase):
    def test_car_details(self):
        car = Car("", "model", 1, 4)
        with   self.assertRaises(Exception) as exception:
            car.make()
        # self.assertEquals(car.model, "model")
        # self.assertEquals(car.fuel_consumption, 1)
        # self.assertEquals(car.fuel_capacity, 4)
