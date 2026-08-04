"""
DEV: Isaac M.D. Brown
Last Iteration: 31/07/2026
"""

from bs4 import BeautifulSoup
import requests
from ..models import Book



class BookStoreClient:
    """Used to pull data from books.toscrape.com, returning the data as Book's"""
    
    # Constants
    BASE_URL: str = "https://books.toscrape.com/"
    CATEGORY_ROUTE: str = "catalogue/category/books/"
    
     
    # Instance variables type hinting
    url: str
    
    def __init__(self):
        """Constructor for BookStoreClient"""
        self.url = self.BASE_URL + self.CATEGORY_ROUTE
    
    def scrape(self, category: str):
        books: list[Book] = []
        
        response = requests.get(self.url + category)

        soup = BeautifulSoup(response.content, 'html.parser')

        book_list = soup.find_all("ol.li")
        
        for li in book_list:
            title_tag = li.find('h3')
            rating_tag = li.find('p')

            if rating_tag:
                rating_tag.get('class')
                        
            if title_tag and rating_tag:
                book = Book(
                    title = title_tag.text,
                    rating = rating_tag.text
                    )
                books.append(book)

        return books

        

        
        


