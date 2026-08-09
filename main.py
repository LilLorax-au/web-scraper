from scrapers.models import Book
from scrapers.services import BookStoreClient




CONTENT_HEAD: str = str(
        "Welcome to the web scraper!\n" + 
        "This program is designed to run through web sites,\n" + 
        "parsing the html,\n" +
        "then doing action with the data.\n" +
        f"The currently use case is targeted at {BookStoreClient.BASE_URL}\n\n" +
        "Lead Dev: Isaac M.D. Brown\n" +
        "Date of last iteration: 30/07/2026\n")






def top_and_tail_content(func):
    def wrapper():
        print(CONTENT_HEAD)

        a_func = func()
                
        return a_func
    return wrapper

@top_and_tail_content
def main():
    
    book_scraper = BookStoreClient()
    
    print("Pulling default and food and drink books, this can take a while :)", flush = True)
    default_books = book_scraper.scrape("default_15")
    food_drink_books = book_scraper.scrape("food-and-drink_33")

    for i, book in enumerate(default_books):
        print(f"{i}.\n{book.to_string(
              use_title = True,
              use_author = False,
              use_rating = True)}", flush = True)

    for i, book in enumerate(food_drink_books):
        print(f"{i}.\n{book.to_string(
              use_title = True,
              use_author = False,
              use_rating = True)}", flush = True)

    return




if __name__ == "__main__":
    main()
