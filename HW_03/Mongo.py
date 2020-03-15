from pymongo import MongoClient
from pprint import pprint

class Mongo:
  def __init__(self, host = 'localhost', port = 27017):
    self.host = host
    self.port = port

    self.client = MongoClient(host, port)
    self.db = self.client['jobs']
    self.coll = self.db.list

  def set_many(self, jobs):
    self.coll.insert_many(jobs)

  def get(self, salaryGT = 0):
    print(salaryGT)
    return self.coll.find({ 'min_price': { '$gte': salaryGT } })
