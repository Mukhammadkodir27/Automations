import requests

# it is getting the content from this url and storing it to this variable
r = requests.get("https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2024-10-27&to=2024-10-31&sortBy=popularity&language=en&apiKey=6c10ecffc6924a218eb6ac45b9d0d96a")
content = r.json()  # converting the content into json format
print(type(content))    # it is a dictionary
print(content["articles"][0]["title"])  # this is what we wanted to get, indexing is used
