from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from w3lib.html import remove_tags
import os
import time

def get_links(html):
  elems = html.find_elements_by_class_name('js-letter-list-item')
  links = []
  for elem in elems:
    links.append(elem.get_attribute('href'))

  return links

def is_exist_class(class_name):
  return WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME, class_name)))

def get_data(driver, link):
  data = {}
  driver.get(link)
  if is_exist_class('layout__content'):
    data['title'] = driver.find_element_by_class_name('thread__subject').text
    data['from'] = driver.find_element_by_class_name('letter-contact').text
    data['date'] = driver.find_element_by_class_name('letter__date').text
    data['body'] = remove_tags(driver.find_element_by_class_name('html-parser').text)

  return data

chrome_options = Options()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(f'{os.getcwd()}/HW_07/venv/chromedriver')
driver.get('https://mail.ru/')

elem = driver.find_element_by_id('mailbox:login')
elem.send_keys('study.ai_172@mail.ru')

elem = driver.find_element_by_id('mailbox:submit')
elem.click()

time.sleep(1)

elem = driver.find_element_by_id('mailbox:password')
elem.send_keys('NewPassword172')

elem = driver.find_element_by_id('mailbox:submit')
elem.click()

if is_exist_class('letter-list'):
  links = get_links(driver)

mails = []
if len(links):
  for link in links:
    data = get_data(driver, link)
    print(data)
    mails.append(data)

driver.quit()