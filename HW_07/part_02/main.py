from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Base import Mongo

import os
import json

chrome_options = Options()
chrome_options.add_argument('--headless')

db = Mongo('mvideo')

driver = webdriver.Chrome(f'{os.getcwd()}/HW_07/venv/chromedriver', options=chrome_options)
driver.get('https://www.mvideo.ru/')

clicks = 0

while True:
  try:
    button = driver.find_elements_by_class_name("sel-hits-button-next")[2]
    if button.get_attribute('class').find('disable') != -1:
      break

    button.click()
    clicks += 1
    print(f'Подгружено {clicks} страниц')
  except Exception as e:
    print('Ошибка: ', e)
    break

goods = driver.find_elements_by_class_name('gallery-list-item')
for good in goods:
  try:
    main = good.find_element_by_class_name('c-product-tile-picture__holder')
  except:
    continue

  data = json.loads(main.find_element_by_tag_name('a').get_attribute('data-product-info'))

  db.set_one(data)
  print(data)
  print('------------------------------------------------------------------------------')


driver.quit()