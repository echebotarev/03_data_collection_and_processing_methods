from pymongo import MongoClient
from pprint import pprint

class Mongo:
  def __init__(self, db, host = 'localhost', port = 27017):
    self.host = host
    self.port = port

    self.client = MongoClient(host, port)
    self.db = self.client[db]
    self.coll = self.db.list

  def set_many(self, data):
    self.coll.insert_many(data)

  def get(self, salaryGT = 0):
    print(salaryGT)
    return self.coll.find({ 'min_price': { '$gte': salaryGT } })
