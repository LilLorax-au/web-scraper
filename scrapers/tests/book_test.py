"""
DEV: Isaac M.D. Brown
Last Iteration: 09/08/2026
"""

import unittest
from ..models import Book


class TestBook(unittest.TestCase):
    """To test the Book class is doing as it should"""

    def setUp(self):
        """Set up for further tests, gives baseline object"""
        self.book_1 = Book(
                title = "Clean Architecture",
                author = "Robert C. Martin",
                rating = "Four"
                )

    def test_book_constructor(self):
        """Test to see if the constructor assigns data correctly"""
        title = "Clean Architecture"
        author = "Robert C. Martin"
        rating = "Four"

        self.assertEqual(self.book_1.title, title)
        self.assertEqual(self.book_1.author, author)
        self.assertEqual(self.book_1.rating, rating)


