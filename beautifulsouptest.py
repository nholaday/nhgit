import requests
from bs4 import BeautifulSoup

data = requests.get('http://www.dota2.com/leaderboards/#americas')

print(data.text)
soup = BeautifulSoup(data.text, 'html.parser')