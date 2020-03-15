import requests
from pprint import pprint

from Vacancies import Vacancies

main_link = 'https://russia.superjob.ru'

vacancy = input('Введите вакансию: ')

v = Vacancies(vacancy)
pprint(v.get())