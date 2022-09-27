import unittest

from project1.plantation import Plantation

class PlantationTest(unittest.TestCase):
    def test_plantation_init(self):
        plantation = Plantation(20)
        self.assertEqual(plantation.size, 20)
        self.assertEqual(plantation.plants, {})
        self.assertEqual(plantation.workers, [])

    def test_plantation_size_below_0(self):
        with self.assertRaises(ValueError) as ex:
            Plantation(-1)
        self.assertEqual(str(ex.exception), "Size must be positive number!")

    def test_worker_hire(self):
        plantation = Plantation(5)
        result =plantation.hire_worker('Peshko')
        self.assertEqual(result, "Peshko successfully hired.")
        self.assertEqual(len(plantation.workers), 1)
        self.assertEqual(plantation.workers[0], 'Peshko')
        with self.assertRaises(ValueError) as ex:
            plantation.hire_worker('Peshko')
        self.assertEqual(str(ex.exception), "Worker already hired!")
        self.assertEqual(len(plantation.workers), 1)
        self.assertEqual(plantation.workers[0], 'Peshko')

    def test_planting(self):
        plantation = Plantation(20)
        with self.assertRaises(ValueError) as ex:
            plantation.planting('Peshko', 'mak')
        self.assertEqual(str(ex.exception), "Worker with name Peshko is not hired!")
        plantation.hire_worker('Peshko')

    def test_str_return(self):
        plantation = Plantation(10)
        expected = "Plantation size: 10"
        actual = str(plantation).strip()
        self.assertEqual(actual, expected)

    def test_repr(self):
        plantation = Plantation(5)
        plantation.hire_worker('Peshko')
        result = repr(plantation)
        expected = 'Size: 5' + '\n'+ 'Workers: Peshko'
        self.assertEqual(result, expected)




