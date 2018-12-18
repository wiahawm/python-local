
import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/index.htm"
headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'youremail@domain.com'  # This is another valid field
}
res = requests.get(url, headers=headers).text
#print(response)

soup = BeautifulSoup(res, 'html.parser')
melons = soup.select('#frm > div > table > tbody')
for melon in melons:
    print(melon.select_one("td:nth-of-type(1) a strong").text)