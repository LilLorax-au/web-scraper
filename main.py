from scrapers.book_store import *



CONTENT_HEAD: str = str(
        "Welcome to the web scraper!\n" + 
        "This program is designed to run through web sites,\n" + 
        "parsing the html,\n" +
        "then doing action with the data.\n" +
        f"The currently use case is targeted at {URL_BASE}\n\n" +
        "Lead Dev: Isaac M.D. Brown\n" +
        "Date of last iteration: 30/07/2026\n")






def top_and_tail_content(func):
    def wrapper():
        print(CONTENT_HEAD)

        a_func = func()
        
        print("FIN")
        return a_func
    return wrapper

@top_and_tail_content
def main():
    print("MID")
    return None




if __name__ == "__main__":
    main()
