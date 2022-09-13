import unittest

from worker import Worker


class WorkerTests(unittest.TestCase):

    def test_name_salary_energy_is_correct_(self):
        person = Worker('name', 100, 1)
        self.assertEqual(person.name, 'name')
        self.assertEqual(person.salary, 100)
        self.assertEqual(person.energy, 1)

    def test_energy_plus_1_after_rest(self):
        person = Worker('name', 100, 1)
        person.rest()
        self.assertEqual(person.energy, 2)
        person.rest()
        self.assertEqual(person.energy, 3)

    def test_work_if_energy_zero(self):
        person = Worker('name', 100, 0)
        with self.assertRaises(Exception) as ex:
            person.work()
        self.assertIsNotNone(ex)

    def test_salary_increase_after_work(self):
        person = Worker('name', 100, 2)
        person.work()
        self.assertEqual(person.money, 100)
        person.work()
        self.assertEqual(person.money, 200)

    def test_energy_decrease_after_work(self):
        person = Worker('name', 100, 1)
        person.work()
        self.assertEqual(person.energy, 0)

    def test_get_info_returns_info(self):
        person = Worker('name', 100, 1)
        self.assertEqual(person.get_info(), f'name has saved 0 money.')


if __name__ == '__main__':
    unittest.main()
