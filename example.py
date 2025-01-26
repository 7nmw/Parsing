from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(r"C:\Users\dinislam\PycharmProjects\pythonProject1\Test-2\chromedriver.exe")

driver.get("https://www.sports.ru/tribuna/blogs/england/3110612.html#supertop")
(driver.find_elements(By.XPATH, "//*[@id=\"branding-layout\"]/div/div/div/main/div/article/div/p/img"))[9].click()
sleep(2)
driver.save_screenshot('sport.png')
driver.quit()
