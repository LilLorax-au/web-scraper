"""
DEV: Isaac M.D. Brown
Last Iteration: 09/08/2026
"""

class ScrapeError(Exception):
    """Raised from failed scrape condition"""
    
    # Default const variables
    DEF_MESSAGE: str = "Scraping failed"
    DEF_STATUS_CODE: int = 0

    def __init__(self, message: str = DEF_MESSAGE, status_code: int = DEF_STATUS_CODE):
        """Using Exception as super class, passing message and adding extra info in self"""
        super().__init__(message)
        self.status_code = status_code

    def __str__(self):
        """Return Exception message and status_code"""
        return f"{self.args[0]} Status Code: {self.status_code}"
    
        

