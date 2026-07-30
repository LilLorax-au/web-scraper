




class Book:
    """A simple model of a book"""

    # default instance vairbles
    DEF_TITLE: str = "Untitled"
    DEF_AURTHER: str = "Nameless"
    DEF_RATING: str = "Zero"
    
    # intsance vairbles type hinting
    title: str
    aurther: str
    rating: str

    def __init__(self, title: str = DEF_TITLE, aurther: str = DEF_AURTHER, rating: str = DEF_RATING):
        """Constructor for book object"""
        self.title = title
        self.aurther = aurther
        self.rating = rating
    
    def __str__(self):
        """Overide for __str__ method, returns a formatted str"""
        return str(
                f"Title: {self.title}\n" +
                f"Aurther: {self.aurther}\n" +
                f"Rating: {self.rating}\n"
                )
        
