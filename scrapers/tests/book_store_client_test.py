"""
DEV: Isaac M.D. Brown
Last Iteration: 09/08/2026
"""

import unittest
from ..services import BookStoreClient
from ..errors import ScrapeError

class TestBookStoreClient(unittest.TestCase):
    """Test to make sure the BookStoreClient is working as intended"""
    def setUp(self):
        """Initial setup, creating baseline object"""
        self.book_store = BookStoreClient()
   
    def test_scrape_no_category(self):
        """Test to check default action for scrape method"""
        self.assertTrue(len(self.book_store.scrape()) > 0, True)
    
    def test_scrape_with_good_category(self):
        """Test to check if scrape returns values on known working category"""
        good_cat_value: str = "food-and-drink_33"
        self.assertTrue(len(self.book_store.scrape(good_cat_value)) > 0, True)
         
    def test_scrape_with_bad_category(self):
        """Test to check if scrape raises error on known not working category"""
        bad_cat_value: str = "food-and-drink_32"

        with self.assertRaises(ScrapeError):
            self.book_store.scrape(bad_cat_value)
                
   
    
