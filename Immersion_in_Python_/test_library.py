import unittest
from library import Library, BookNotFoundError

class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library()

    def test_add_book(self):
        self.library.add_book("Python Programming")
        self.assertIn("Python Programming", self.library.list_books())

    def test_remove_book(self):
        self.library.add_book("Python Programming")
        self.library.remove_book("Python Programming")
        self.assertNotIn("Python Programming", self.library.list_books())

    def test_remove_nonexistent_book(self):
        with self.assertRaises(BookNotFoundError):
            self.library.remove_book("Nonexistent Book")

    def test_list_books(self):
        self.library.add_book("Python Programming")
        self.library.add_book("Data Science")
        self.library.remove_book("Python Programming")
        self.assertEqual(self.library.list_books(), ["Data Science"])

if __name__ == "__main__":
    unittest.main()