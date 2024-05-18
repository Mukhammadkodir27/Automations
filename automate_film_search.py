import webbrowser
import urllib.parse


def construct_search_url(movie_name, site):
    if site == "fmovies":
        base_url = "https://fmovies.to/search?keyword="
    elif site == "kinogo":
        base_url = "https://kinogo.biz/index.php?do=search&subaction=search&story="
    else:
        raise ValueError("Unsupported site.")

    query = urllib.parse.quote_plus(movie_name)
    return base_url + query


def open_movie_search(movie_name):
    sites = ["fmovies", "kinogo"]
    search_urls = []

    for site in sites:
        try:
            search_url = construct_search_url(movie_name, site)
            search_urls.append(search_url)
        except ValueError as e:
            print(e)

    # Open search results in web browser tabs
    for url in search_urls:
        webbrowser.open_new_tab(url)


def main():
    print("Welcome to the Movie Search Automation App!")
    movie_name = input("Enter the name of the film or movie: ")

    print(f"Searching for '{movie_name}' on supported websites...")
    open_movie_search(movie_name)
    print("Search results have been opened in your browser.")


if __name__ == "__main__":
    main()
