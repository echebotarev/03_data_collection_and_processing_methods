import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import requests
from pprint import pprint

from HW_03.Mongo import Mongo
mongo = Mongo('jobs')

from Vacancies import Vacancies

vacancy = input('Введите вакансию: ')

v = Vacancies(vacancy)

vacancies = v.get()
pprint(vacancies)

mongo.set_many(vacancies)

for job in mongo.get(100000):
  pprint(job)
