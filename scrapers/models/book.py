"""
DEV: Isaac M.D. Brown
Last Iteration: 30/07/2026
"""

class Book:
    """A simple model of a book"""

    # default instance variables
    DEF_TITLE: str = "Untitled"
    DEF_AUTHOR: str = "Nameless"
    DEF_RATING: str = "Zero"
    
    # instance variables type hinting
    title: str
    author: str
    rating: str

    def __init__(self, title: str = DEF_TITLE, author: str = DEF_AUTHOR, rating: str = DEF_RATING):
        """Constructor for book object"""
        self.title = title
        self.author = author
        self.rating = rating
    
    def __str__(self, use_title: bool = True, use_author: bool = True, use_rating: bool = True):
        """Override for __str__ method, returns a formatted str"""
        book_state: str = ""
        
        if use_title:
            book_state += f"Title: {self.title}\n"                
        if use_author:
            book_state += f"Author: {self.author}\n"
        if use_rating:
            book_state += f"Rating: {self.rating}\n"
        
        return book_state

    def to_string(self, use_title: bool, use_author: bool, use_rating: bool):
        """
        Addional str method to give options on what intance variables get returned,
        saves unessesy access to __str__
        """
        return self.__str__(use_title, use_author, use_rating)

        
