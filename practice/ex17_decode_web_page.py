# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/"
r = requests.get(url)
r_html = r.text.encode('utf-8')

# nyt1 = open("text1.html", "w")
# nyt1.write(r_html)
# nyt1.close()

soup = BeautifulSoup(r_html, 'html.parser')
# nyt2 = open("text2.html", "w")
# nyt2.write(soup.prettify().encode('utf-8'))
# nyt2.close()

titles = []
for title in soup.find_all(class_="story-heading"):
    titles.append(title.get_text().encode('utf-8'))

for i in titles:
    print i
