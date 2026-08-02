"""
DEV: Isaac M.D. Brown
Last Iteration: 31/07/2026
"""

from bs4 import BeautifulSoup
import requests
from ..models import Book



class BookStoreClient:
    """Used to pull data from books.toscrape.com, storing the data as Book's"""
    
    # Constants
    BASE_URL: str = "https://books.toscrape.com/"
    CATEGORY_ROUTE: str = "catalogue/category/books/"
    
    # Default instance variables
    DEF_CATEGORY: str = ""
    DEF_URL_OVERRIDE: str | None = None
    
    # Instance variables type hinting
    category: str
    url_override: str
    url: str

    def __init__(self, category: str = DEF_CATEGORY, url_override: str | None = DEF_URL_OVERRIDE):
        """Constructor for BookStoreClient"""
        if category:
        self.category = category
        

        
        


