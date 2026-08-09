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
    # only use for declared categories
    CATEGORY_ROUTE: str = "catalogue/category/books/"
    
    # use only on if scrape() has no parameter passed, is default book age
    DEF_CATEGORY_ROUTE: str = "https://books.toscrape.com/catalogue/category/books_1/"    
     
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
            print(page_i)

            if category:
                response = requests.get(self.url + category + f"page-{page_i}.html")
            else:
                response = requests.get(self.DEF_CATEGORY_ROUTE + f"page-{page_i}.html")

            if response.status_code == 200:
                
                soup = BeautifulSoup(response.content, 'html.parser')

                ordered_list_block = soup.find("ol")

                book_list = ordered_list_block.find_all("li")
                
                title: str = ''
                rating: str = ''
                
                for li in book_list:
                    title_tag = li.find('h3')
                    rating_tag = li.find('p')

                    if title_tag:
                        title = title_tag.text

                    if rating_tag:
                        rating_tag = rating_tag.get('class')
                    if rating_tag:
                        rating = rating_tag[-1]
                    
                    if title_tag and rating_tag:
                        book = Book(
                            title = title_tag.text,
                            rating = rating_tag[-1]
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

        

        
        


