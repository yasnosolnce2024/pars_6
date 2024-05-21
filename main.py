import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = 'https://www.divan.ru/kemerovo/category/svet'
driver.get(url)
time.sleep(3)

lihts = driver.find_elements(By.CLASS_NAME, 'lsooF')

parsed_data = []

for light in lihts:
    try:
        title = light.find_element(By.CSS_SELECTOR, 'span').text
        price = light.find_element(By.CSS_SELECTOR, 'meta').get_attribute('content')
        link = light.find_element(By.CSS_SELECTOR, 'link').get_attribute('href')
        parsed_data.append([title, price, link])
    except:
        print("произошла ошибка при парсинге")
        continue

driver.quit()

with open("hh.csv", 'w',newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название светильника', 'цена', 'web ссылка'])
    writer.writerows(parsed_data)
