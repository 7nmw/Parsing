import time

import requests
from bs4 import BeautifulSoup

# HTML - парсинг с BS
# Найти API
# Selenuim



bank_url = 'https://www.forabank.ru/exchange/'
bank_data = requests.get(bank_url)
print(bank_data.status_code)

bank_soup = BeautifulSoup(bank_data.content, "html.parser")
elements = bank_soup.findAll(class_="content-right-courses-item-value.-arr")

for element in elements:
    print(elements)
