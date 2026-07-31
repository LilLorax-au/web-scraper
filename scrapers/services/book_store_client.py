"""
DEV: Isaac M.D. Brown
Last Iteration: 31/07/2026
"""

from bs4 import BeautifulSoup
import requests
from ..models import Book



class BookStoreClient:
    """Used to pull data from books.toscrape.com"""
    
    BASE_URL: str = "https://books.toscrape.com/"
