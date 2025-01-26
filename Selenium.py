from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

browser = webdriver.Chrome() # Открываем
browser.get("https://www.ozon.ru/category/odeyala-15081/")

print(browser.title)

# Делаем филтьтр
Filter_Ozon = '//*[@id="layoutPage"]/div[1]/div[2]/div[2]/div[1]/div/aside/div[10]/div[2]/div/a[1]'
filter = browser.find_element(by=By.XPATH, value=Filter_Ozon)
filter.click()


# Найдет все цены
XPATH_price = '//*[@id="paginatorContent"]/div/div/div[10]/div[1]'
elements = browser.find_elements(by=By.XPATH, value=XPATH_price)
className = elements[0].get_attribute("class")
prices = browser.find_elements(by=By.CSS_SELECTOR, value=f"span[class='{className}']")
print(len(prices))
for element in prices:
    parent1 = element.find_element(by=By.XPATH, value="..")
    parent2 = element.find_element(by=By.XPATH, value="..")
    try:
        print(element.text)
        print(element.parent.parent.find_elements(by=By.TAG_NAME, value="a").text)
    except:
        print("Error")



'''
XPATH_links = '//*[@id="paginatorContent"]/div/div/div[4]/a'
elements = browser.find_elements(by=By.XPATH, value=XPATH_links)
className = elements[0].get_attribute("class")
links = browser.find_elements(by=By.CSS_SELECTOR, value=f"span[class='{className}']")
print(len(links))
for element in links:
    element.click()
'''

time.sleep(15)
browser.close()