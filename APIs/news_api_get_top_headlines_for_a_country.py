import requests

# # it is getting the content from this url and storing it to this variable
# r = requests.get("https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2024-10-27&to=2024-10-31&sortBy=popularity&language=en&apiKey=6c10ecffc6924a218eb6ac45b9d0d96a")
# content = r.json()  # converting the content into json format   # it is a dictionary
# articles = content["articles"]

#! what i have changed here was removing topic, date, and language
#! instead wrote top-headlines?country={country} and then API key, this gives todays news for any country


def get_news(country, api_key="6c10ecffc6924a218eb6ac45b9d0d96a"):
    url = f"https://newsapi.org/v2/top-headlines?country={
        country}&apiKey={api_key}"
    r = requests.get(url)
    content = r.json()
    articles = content["articles"]
    results = []
    for article in articles:
        results.append(f"Title:--------------- {article['title']}, \t  \n Description:-------------- {
                       article['description']}")
    return results


def main():
    country = input("Enter topic name: ")
    print(get_news(country=country))


main()
