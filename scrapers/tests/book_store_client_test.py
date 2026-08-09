import unittest
from ..services import BookStoreClient
from ..errors import ScrapeError

class TestBookStoreClient(unittest.TestCase):

    def setUp(self):
        self.book_store = BookStoreClient()
   
    def test_scrape_no_category(self):
        self.assertTrue(len(self.book_store.scrape()) > 0, True)
    
    def test_scrape_with_good_category(self):
        good_cat_value: str = "food-and-drink_33"
        self.assertTrue(len(self.book_store.scrape(good_cat_value)) > 0, True)
         
    def test_scrape_with_bad_category(self):
        bad_cat_value: str = "food-and-drink_32"

        with self.assertRaises(ScrapeError):
            self.book_store.scrape(bad_cat_value)
                
   
    
