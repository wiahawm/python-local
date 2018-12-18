import requests
from bs4 import BeautifulSoup

url = "http://m.exchange.daum.net/mobile/exchange/exchangeMain.daum"
res = requests.get(url).text
soup = BeautifulSoup(res, 'html.parser')

coins = soup.select('#asiaBody > table > tbody')
coins2 = soup.select('#europeBody > table > tbody')

for coin in coins:
    print(coin.text)

for coin in coins2:
    print(coin.text)
    #print(coin.select_one("td:nth-of-type(1) strong"))
    #print(coin.select("td:nth-of-type(2) strong"))
    #print(coin)
