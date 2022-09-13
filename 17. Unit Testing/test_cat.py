'''
•	Cat is not sleepy after sleeping

'''
import unittest

from cat import Cat


class CatTest(unittest.TestCase):
    cat = Cat('Kotinka')

    def test_size_increase_after_eating(self):
        cat = Cat('Kotinka')
        cat.eat()
        self.assertEqual(cat.size, 1)

    def test_fed_istrue_after_eating(self):
        cat = Cat('Kotinka')
        cat.eat()
        self.assertTrue(cat.fed)

    def test_eat_after_eating_is_false(self):
        cat = Cat('Kotinka')
        cat.eat()
        with self.assertRaises(Exception) as ex:
            cat.eat()
        self.assertIsNotNone(ex)

    def test_sleep_error_if_not_fed(self):
        cat = Cat('Kotinka')
        with self.assertRaises(Exception) as ex:
            cat.sleep()

    def test_sleep_error_after_sleeping(self):
        cat = Cat('Kotinka')
        cat.eat()
        cat.sleep()
        self.assertFalse(cat.sleepy)

if __name__ == '__main__':
    unittest.main()