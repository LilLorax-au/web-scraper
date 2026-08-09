import unittest
from ..models import Book




class TestBook(unittest.TestCase):

    def setUp(self):
        self.book_1 = Book(
                title = "Clean Architecture",
                author = "Robert C. Martin",
                rating = "Four"
                )

    def test_book_constructor(self):
        title = "Clean Architecture"
        author = "Robert C. Martin"
        rating = "Four"

        self.assertEqual(self.book_1.title, title)
        self.assertEqual(self.book_1.author, author)
        self.assertEqual(self.book_1.rating, rating)


