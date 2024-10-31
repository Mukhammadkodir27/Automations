import requests

# # it is getting the content from this url and storing it to this variable
# r = requests.get("https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2024-10-27&to=2024-10-31&sortBy=popularity&language=en&apiKey=6c10ecffc6924a218eb6ac45b9d0d96a")
# content = r.json()  # converting the content into json format   # it is a dictionary
# articles = content["articles"]


def get_news(topic, from_date, to_date, language="en", api_key="6c10ecffc6924a218eb6ac45b9d0d96a"):
    url = f"https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={
        to_date}&sortBy=popularity&language={language}&apiKey={api_key}"
    r = requests.get(url)
    content = r.json()
    articles = content["articles"]
    results = []
    for article in articles:
        results.append(f"Title:--------------- {article['title']}, \t  \n Description:-------------- {
                       article['description']}")
    return results


def main():
    topic = input("Enter topic name: ")
    from_date = input("Enter from date: ")
    to_date = input("Enter end date: ")
    print(get_news(topic=topic, from_date=from_date, to_date=to_date))


main()
