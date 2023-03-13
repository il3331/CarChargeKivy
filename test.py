import requests
from bs4 import BeautifulSoup

url = 'https://yandex.ru/map-widget/v1/?um=constructor%3Acd293d31b30a2158f34d16fd9cf7ac4d055f720abb6b8b01338905ee0f9660a7&source=constructor'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

full_page = requests.get(url, headers)

soup = BeautifulSoup(full_page.content,'html.parser')
convert = soup.findAll("div", {"class": "map-container"})

print(convert)