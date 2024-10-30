from bs4 import BeautifulSoup
import requests


def get_currency(in_currency, out_currency, amount):
    url = f"https://www.x-rates.com/calculator/?from={
        in_currency}&to={out_currency}&amount={amount}"
    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")
    rate = soup.find("span", class_="ccOutputRslt").get_text()
    rate = float(rate.replace(',', '')[:-4])
    return rate


in_currency = input("Enter in currency: ")
out_currency = input("Out Currency: ")
amount = float(input("Enter amount: "))
current_rate = get_currency(in_currency, out_currency, amount)
print(f"{current_rate} {out_currency}")

print(type(in_currency))
print(type(amount))
