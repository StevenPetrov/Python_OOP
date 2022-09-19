from project.movie import Movie
import unittest

class Movietest(unittest.TestCase):
    def test_movie_attributes(self):
        movie = Movie('name', 2000, 9.9)
        self.assertEqual(movie.name, 'name')
        self.assertEqual(movie.year, 2000)
        self.assertEqual(movie.rating, 9.9)
        self.assertEqual(movie.actors, [])


    def test_movie_name_input_verify(self):
        with self.assertRaises(ValueError) as ex:
            Movie('', 2000, 9.9)
        self.assertEqual(str(ex.exception), "Name cannot be an empty string!")

    def test_movie_with_year_before_1887_verify(self):
        with self.assertRaises(ValueError) as ex:
            Movie('name', 1886, 9.9)
        self.assertEqual(str(ex.exception), "Year is not valid!")

    def test_add_actor_func(self):
        movie = Movie('name', 2000, 9.9)
        movie.add_actor('Peshko')
        self.assertEqual(movie.actors[0], 'Peshko')
        movie.add_actor('Goshko')
        self.assertEqual(movie.actors[1], 'Goshko')
        self.assertEqual(len(movie.actors), 2)
        self.assertEqual(movie.add_actor('Goshko'), f"Goshko is already added in the list of actors!")
        self.assertEqual(len(movie.actors), 2)

    def test_repr(self):
        movie = Movie('name', 2000, 9.9)
        movie.add_actor('Peshko')
        movie.add_actor('Goshko')

        expected = f"Name: name\n" \
               f"Year of Release: {2000}\n" \
               f"Rating: {9.9:.2f}\n" \
               f"Cast: Peshko, Goshko"

        actual = f"Name: {movie.name}\n" \
               f"Year of Release: {movie.year}\n" \
               f"Rating: {movie.rating:.2f}\n" \
               f"Cast: {', '.join(movie.actors)}"

        self.assertEqual(expected, actual)

    def test_compare_two_movies(self):
        movie = Movie('name', 2000, 9.9)
        movie2 = Movie('name2', 2000, 9.1)

        expected = f'"name" is better than "name2"'
        actual = movie > movie2

        self.assertEqual(expected, actual)

        expected = f'"name" is better than "name2"'
        actual = movie2 > movie

        self.assertEqual(expected, actual)

