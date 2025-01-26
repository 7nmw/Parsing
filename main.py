import requests
from bs4 import BeautifulSoup

skillbox = requests.get("https://live.skillbox.ru/") # Получаем ответ от сайта скиллбокс

print(skillbox.status_code)


skillSoup = BeautifulSoup(skillbox.content, "html.parser")  # Разбираем код станицы на элементы
webinars = skillSoup.findAll(class_="webinar-card__title t t--4")  # Находим все элементы с указаным классом

print([webinar.string.strip() for webinar in webinars])

# Сделаем парсинг, получим даты

webinarsFull = skillSoup.findAll(class_="webinars__item")
for webinar in webinarsFull:  # Код обработки каждого вебинара
    title = webinar.find(class_="webinar-card__title t t--4").string.strip()
    date = webinar.find(class_="webinar-card__date f f--12").string.strip()
    print(f"Вебинар {title} пройтед {date}")
