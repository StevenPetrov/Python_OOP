import unittest

from project.bookstore import Bookstore

class Bookstoretest(unittest.TestCase):
    def test_text_init_methods(self):
        bookstore = Bookstore(5)
        self.assertEqual(bookstore.books_limit, 5)
        self.assertEqual(bookstore.total_sold_books, 0)
        expected = "Total sold books: 0"+ '\n' "Current availability: 0"
        self.assertEqual(str(bookstore), expected)

    def test_if_negative_books(self):
        with self.assertRaises(ValueError) as ex:
            Bookstore(-1)
        self.assertEqual(str(ex.exception), f"Books limit of -1 is not valid")

    def test_len_correct_and_negative(self):
        bookstore = Bookstore(5)
        self.assertEqual(len(bookstore), 0)
        bookstore.receive_book('book1', 2)
        self.assertEqual(len(bookstore), 2)
        bookstore.receive_book('book1', 2)
        self.assertEqual(len(bookstore), 4)

    def test_receive_books_oversize(self):
        bookstore = Bookstore(5)
        result = bookstore.receive_book('book1', 1)
        self.assertEqual(result, f"{1} copies of {'book1'} are available in the bookstore.")
        self.assertEqual(bookstore.availability_in_store_by_book_titles, {'book1': 1})
        with self.assertRaises(Exception) as ex:
            bookstore.receive_book('book1', 10)
        self.assertEqual(str(ex.exception), f"Books limit is reached. Cannot receive more books!")
        self.assertEqual(result, f"{1} copies of {'book1'} are available in the bookstore.")
        self.assertEqual(bookstore.total_sold_books, 0)

    def test_sell_book_cases(self):
        bookstore = Bookstore(5)
        bookstore.receive_book('book1', 4)
        result = bookstore.sell_book('book1', 2)
        self.assertEqual(result, f"Sold {2} copies of {'book1'}")
        self.assertEqual(bookstore.availability_in_store_by_book_titles, {'book1': 2})
        with self.assertRaises(Exception) as ex:
            bookstore.sell_book('book1', 4)
        self.assertEqual(str(ex.exception), f"{'book1'} has not enough copies to sell. Left: {2}")
        self.assertEqual(bookstore.availability_in_store_by_book_titles, {'book1': 2})
        with self.assertRaises(Exception) as ex:
            bookstore.sell_book('book2', 4)
        self.assertEqual(str(ex.exception), f"Book {'book2'} doesn't exist!")
        self.assertEqual(bookstore.availability_in_store_by_book_titles, {'book1': 2})
        self.assertEqual(bookstore.total_sold_books, 2)

    def test_str_method(self):
        bookstore = Bookstore(5)
        expected = "Total sold books: 0"+ '\n' "Current availability: 0"
        self.assertEqual(str(bookstore), expected)
        bookstore.receive_book('book1', 4)
        expected = "Total sold books: 0"+ '\n' "Current availability: 4" + '\n' " - book1: 4 copies"
        self.assertEqual(str(bookstore), expected)
        bookstore.sell_book('book1', 2)
        expected = "Total sold books: 2"+ '\n' "Current availability: 2" + '\n' " - book1: 2 copies"
        self.assertEqual(str(bookstore), expected)


