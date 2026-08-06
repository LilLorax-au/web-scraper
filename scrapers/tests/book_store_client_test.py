import unittest
from ..services import BookStoreClient

class TestBookStoreClient(unittest.TestCase):

    def SetUp(self):
        self.book_store = BookStoreClient()

    def test_scrape_no_category(self):
        self.book_store = BookStoreClient()
        self.assertTrue(len(self.book_store.scrape()) > 0, True)

