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
        self.aurthor = author
        self.rating = rating
    
    def __str__(self):
        """Override for __str__ method, returns a formatted str"""
        return str(
                f"Title: {self.title}\n" +
                f"Author: {self.author}\n" +
                f"Rating: {self.rating}\n"
                )
        
