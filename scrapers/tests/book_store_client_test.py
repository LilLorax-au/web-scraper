import unittest
from ..services import BookStoreClient

class TestBookStoreClient(unittest.TestCase):

    def SetUp(self):
        self.book_store = BookStoreClient()
    

    def test_scrape_no_category(self):
        self.assertTrue(len(self.book_store.scrape()) > 0, True)
    
    def test_scrape_with_good_category(self):
        self.assertTrue(len(self.book_store.scrape("food-and-drink_33")) > 0, True)
        
    def test_scrape_with_bad_category(self):
        with self.assertRaises(Exception):
            pass
                
   
    
