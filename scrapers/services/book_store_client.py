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
    # only use for decared categories
    CATEGORY_ROUTE: str = "catalogue/category/books/"
    
    # use only on if scrape() has no parameter passed, is default book age
    DEF_CATEGORY_ROUTE: str = "catalogue/category/books_1/"    
     
    # Instance variables type hinting
    url: str
    
    def __init__(self):
        """Constructor for BookStoreClient"""
        self.url = self.BASE_URL + self.CATEGORY_ROUTE
    
    def scrape(self, category: str = ''):
        books: list[Book] = []
        page_i = 0
        
        while True:
            page_i += 1

            if category:
                response = requests.get(self.url + category + f"page_{page_i}")
            else:
                response = requests.get(self.DEF_CATEGORY_ROUTE + f"page_{page_i}")

            if response.status_code == 200:

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
            else:
                if len(books) == 0:
                    raise Exception(
                            "Error, scrape failed, " + 
                            "response status_code: " + 
                            str(response.status_code)
                            )
                else:
                    break

        return books

        

        
        


