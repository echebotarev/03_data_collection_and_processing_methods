import requests
from pprint import pprint

from Vacancies import Vacancies

vacancy = input('Введите вакансию: ')

v = Vacancies(vacancy)
pprint(v.get())