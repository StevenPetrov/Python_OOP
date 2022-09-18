import unittest

from EXAM_PREP_1.hero import Hero

class HeroTests(unittest.TestCase):
    def setUp(self) -> None:
        self.hero = Hero('hero', 5, 100, 10)
        self.enemy = Hero('enemy', 5, 100, 10)

    def test_initialize(self):
        self.assertEqual(self.hero.username, 'hero')
        self.assertEqual(self.hero.level, 5)
        self.assertEqual(self.hero.health, 100)
        self.assertEqual(self.hero.damage, 10)

    def test_cannot_battle_urself(self):
        temp_enemy = Hero('hero', 5, 50, 10)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(temp_enemy)
        self.assertEqual(str(ex.exception), "You cannot fight yourself")

    def test_fight_when_hp_is_zero(self):
        hero = Hero('hero', 5, 0, 10)
        with self.assertRaises(ValueError) as ex:
            hero.battle(self.enemy)
        self.assertEqual(str(ex.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_fight_zero_hp_enemy(self):
        enemy_hero = Hero('enemy', 5, 0, 10)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual(str(ex.exception), f"You cannot fight {enemy_hero.username}. He needs to rest")

    def test_if_draw(self):
        hero = Hero('hero', 10, 100, 10)
        enemy = Hero('enemy', 10, 100, 10)
        self.assertEqual(hero.battle(enemy), 'Draw')
        self.assertEqual(hero.health, enemy.health)

    def test_if_attacker_wins(self):
        hero = Hero('hero', 10, 100, 10)
        enemy = Hero('enemy', 1, 10, 10)
        self.assertEqual(hero.battle(enemy), 'You win')
        self.assertEqual(hero.level, 11)
        self.assertEqual(hero.health, 95)
        self.assertEqual(hero.damage, 15)

    def test_if_attacker_loses(self):
        hero = Hero('hero', 10, 100, 10)
        enemy = Hero('enemy', 1, 1000, 10)
        self.assertEqual(hero.battle(enemy), 'You lose')
        self.assertEqual(enemy.level, 2)
        self.assertEqual(enemy.health, 905)
        self.assertEqual(enemy.damage, 15)

    def test_str_method(self):
        hero = Hero('hero', 10, 100, 10)
        actual = str(hero)
        expected = f"Hero hero: 10 lvl\n" \
               f"Health: 100\n" \
               f"Damage: 10\n"
        self.assertEqual(actual,expected)

if __name__ == '__main__':
    unittest.main()