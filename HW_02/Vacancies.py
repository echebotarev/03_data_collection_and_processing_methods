from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint

superjob_link = 'https://russia.superjob.ru'
superjob_searched_link = '/vacancy/search/?keywords='

hh_link = 'https://hh.ru'
hh_searched_link = '/search/vacancy?clusters=true&enable_snippets=true&salary=&st=searchVacancy&text='

def get_digits(input):
  output = ''
  for i in filter(str.isdigit, input) : output = output + i
  return output if output else None

def get_currency(price):
  if not price:
    return None

  currencies = ['USD', 'KZT', 'руб.', '₽', 'EUR']
  for currency in currencies:
    if currency in price:
      return currency

  return None

def get_price(price, priceType):
  if not price:
    return price

  if 'По договорённости' in price:
    price = None

  elif 'от' in price:
    price = get_digits(price) if priceType == 'min' else None

  elif 'до' in price:
    price = None if priceType == 'min' else get_digits(price)

  elif '-' in price:
    price = get_digits(price.split('-')[0]) if priceType == 'min' else get_digits(price.split('-')[1])

  elif '—' in price:
    price = get_digits(price.split('—')[0]) if priceType == 'min' else get_digits(price.split('—')[1])

  elif get_digits(price):
    price = get_digits(price)

  else:
    price = None

  return price + currency if price and currency else price

def get_vacancy_name(site, vacancy):
  if site == 'hh':
    return vacancy.replace(' ', '+')
  else: 
    return vacancy.replace(' ', '%20')

def get_url(site, vacancy, page):
  if site == 'hh':
    return f'{hh_link}{hh_searched_link}{vacancy}&page={page}'
  else:
    return f'{superjob_link}{superjob_searched_link}{vacancy}&page={page}'

def get_vacancy_list(site, html):
  if site == 'hh':
    return html.find_all('div', {'class': 'vacancy-serp-item'})
  else:
    return html.find_all('div', {'class': 'QiY08 LvoDO'})

def get_vacancy_data(site, vacancy):
  vacancy_data = {}

  if site == 'superjob':
    name = vacancy.find('a', {'class': 'icMQ_'})
    vacancy_data['name'] = name.getText() if name else None
    vacancy_data['link'] = superjob_link + name['href'] if name else None
    vacancy_data['site'] = superjob_link

    price = vacancy.find('span', {'class': 'f-test-text-company-item-salary'})
    vacancy_data['price'] = price.getText() if price else None

    vacancy_data['min_price'] = get_price(vacancy_data['price'], 'min')
    vacancy_data['max_price'] = get_price(vacancy_data['price'], 'max')

    vacancy_data['currency'] = get_currency(vacancy_data['price'])

    return vacancy_data

  link = vacancy.find('a', attrs = {'data-qa': 'vacancy-serp__vacancy-title'})
  vacancy_data['name'] = link.getText() if link else None
  vacancy_data['link'] = link['href'] if link else None
  vacancy_data['site'] = hh_link

  price = vacancy.find('span', attrs = {'data-qa': 'vacancy-serp__vacancy-compensation'})
  vacancy_data['price'] = price.getText() if price else None

  vacancy_data['min_price'] = get_price(vacancy_data['price'], 'min')
  vacancy_data['max_price'] = get_price(vacancy_data['price'], 'max')

  vacancy_data['currency'] = get_currency(vacancy_data['price'])

  return vacancy_data

def get_vacancies(site, vacancy, page):
  if not vacancy:
    return None

  vacancy = get_vacancy_name(site, vacancy)

  url = get_url(site, vacancy, page)

  html = requests.get(
    url,
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
  ).text

  vacancy_list = get_vacancy_list(site, bs(html, 'lxml'))

  vacancies = []
  for vacancy in vacancy_list:
    vacancies.append(get_vacancy_data(site, vacancy))

  return vacancies

class Vacancies:
  def __init__(self, vacancy):
    self.vacancy = vacancy

  def get(self):
    output = []

    i = 1
    while(True):
      vacancies = get_vacancies('superjob', self.vacancy, i)

      if not len(vacancies):
        break

      output = output + vacancies
      i = i + 1

    i = 1
    while(True):
      vacancies = get_vacancies('hh', self.vacancy, i)

      if not len(vacancies):
        break

      output = output + vacancies
      i = i + 1

    return output