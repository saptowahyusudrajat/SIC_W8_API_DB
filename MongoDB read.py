import pymongo
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://saptowahyusudrajat:1331@cluster0.eqvtb81.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(uri)
db = client['test_SIC'] # ganti sesuai dengan nama database kalian
my_collections = db['col1'] # ganti sesuai dengan nama collections kalian

for x in my_collections.find():
  print(x)
