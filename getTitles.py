import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

# get all titles
titles = soup.find_all('title')

for title in titles:
    print(title.text)
